"""Production-ready tech stack recommender for the tech_stacks.csv dataset."""

from __future__ import annotations

import argparse
import logging
import os
from dataclasses import dataclass
from typing import List, Optional

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


DEFAULT_DATASET_PATH = "tech_stacks.csv"
DEFAULT_TOP_N = 5
REQUIRED_COLUMNS = {
    "id",
    "tech_stack",
    "category",
    "level",
    "skills",
    "description",
}


@dataclass
class Recommendation:
    id: int
    tech_stack: str
    category: str
    level: str
    skills: str
    description: str
    score: float


class RecommendationEngine:
    def __init__(self, csv_path: str) -> None:
        self.csv_path = csv_path
        self.df: Optional[pd.DataFrame] = None
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.tfidf_matrix = None

    def load_data(self) -> None:
        if not os.path.exists(self.csv_path):
            raise FileNotFoundError(f"Dataset not found: {self.csv_path}")

        df = pd.read_csv(self.csv_path)
        df.columns = [column.strip().lower() for column in df.columns]

        missing_columns = REQUIRED_COLUMNS - set(df.columns)
        if missing_columns:
            raise ValueError(
                "Missing required columns: " + ", ".join(sorted(missing_columns))
            )

        text_columns = ["tech_stack", "category", "level", "skills", "description"]
        for column in text_columns:
            df[column] = df[column].fillna("").astype(str).str.strip()

        df["id"] = pd.to_numeric(df["id"], errors="coerce").fillna(0).astype(int)
        df["search_text"] = df[text_columns].agg(" ".join, axis=1).str.lower()
        self.df = df

        logging.info("Loaded %d tech stack rows from %s", len(df), self.csv_path)

    def train(self) -> None:
        if self.df is None:
            raise RuntimeError("Dataset must be loaded before training.")

        self.tfidf_matrix = self.vectorizer.fit_transform(self.df["search_text"])
        logging.info("TF-IDF model trained on %d records", len(self.df))

    def recommend(self, user_input: str, top_n: int = DEFAULT_TOP_N) -> List[Recommendation]:
        if self.df is None or self.tfidf_matrix is None:
            raise RuntimeError("Model is not ready. Call load_data() and train() first.")

        cleaned_input = user_input.strip().lower()
        if not cleaned_input:
            raise ValueError("Input cannot be empty.")

        user_vector = self.vectorizer.transform([cleaned_input])
        similarity_scores = cosine_similarity(user_vector, self.tfidf_matrix).flatten()

        ranked_indices = similarity_scores.argsort()[::-1][:top_n]
        recommendations: List[Recommendation] = []

        for index in ranked_indices:
            row = self.df.iloc[index]
            recommendations.append(
                Recommendation(
                    id=int(row["id"]),
                    tech_stack=str(row["tech_stack"]),
                    category=str(row["category"]),
                    level=str(row["level"]),
                    skills=str(row["skills"]),
                    description=str(row["description"]),
                    score=round(float(similarity_scores[index]), 4),
                )
            )

        return recommendations


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Recommend tech stacks from the tech_stacks.csv dataset."
    )
    parser.add_argument(
        "--csv",
        default=DEFAULT_DATASET_PATH,
        help="Path to the tech stacks dataset CSV.",
    )
    parser.add_argument(
        "--query",
        default=None,
        help="User skills or interests used for matching.",
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=DEFAULT_TOP_N,
        help="Number of recommendations to return.",
    )
    return parser


def format_recommendations(recommendations: List[Recommendation]) -> None:
    print("\nTop recommendations:\n")
    for index, recommendation in enumerate(recommendations, start=1):
        print(f"{index}. {recommendation.tech_stack} ({recommendation.score:.4f})")
        print(f"   Category: {recommendation.category} | Level: {recommendation.level}")
        print(f"   Skills: {recommendation.skills}")
        print(f"   Description: {recommendation.description}\n")


def main() -> None:
    parser = build_argument_parser()
    args = parser.parse_args()

    engine = RecommendationEngine(args.csv)
    engine.load_data()
    engine.train()

    query = args.query or input("Enter your skills, interests, or target role: ")
    recommendations = engine.recommend(query, top_n=args.top_n)

    if not recommendations:
        print("No recommendations found.")
        return

    format_recommendations(recommendations)


if __name__ == "__main__":
    main()