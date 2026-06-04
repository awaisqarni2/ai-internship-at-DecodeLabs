# Tech Stack Recommendation System

Production-ready, CSV-driven recommendation system for matching a user’s skills, interests, or target role to the most relevant tech stack in `tech_stacks.csv`.

## Overview

This project uses a lightweight TF-IDF + cosine similarity approach to rank rows in the dataset against a natural-language query. Each recommendation includes the tech stack name, category, level, skills, description, and a similarity score.

The system is designed to be easy to run locally, simple to extend, and safe to use from the command line.

## Project Files

- `production_recommendation_system.py` - main recommender script
- `tech_stacks.csv` - dataset used for recommendations

## Features

- Loads and validates the CSV dataset before training
- Combines tech stack metadata into a single searchable text field
- Ranks results using TF-IDF vectorization and cosine similarity
- Supports both interactive input and command-line queries
- Returns structured recommendations with scores

## Requirements

- Python 3.9 or newer
- `pandas`
- `scikit-learn`

## Installation

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install pandas scikit-learn
```

If you already use Conda:

```bash
conda create -n tech-recommender python=3.10 pandas scikit-learn
conda activate tech-recommender
```

## Dataset Format

The recommender expects these columns in `tech_stacks.csv`:

- `id`
- `tech_stack`
- `category`
- `level`
- `skills`
- `description`

Example row:

```csv
1,Python Developer,Backend,Beginner,"python flask django api backend sql","Build backend applications and APIs using Python frameworks."
```

## Usage

Run the recommender with the default dataset:

```bash
python production_recommendation_system.py
```

Pass a query directly from the command line:

```bash
python production_recommendation_system.py --query "I want to build APIs with Python and SQL"
```

Use a different dataset path if needed:

```bash
python production_recommendation_system.py --csv tech_stacks.csv --query "machine learning and NLP"
```

Choose how many results to return:

```bash
python production_recommendation_system.py --query "cloud automation" --top-n 3
```

## Example Output

```text
Top recommendations:

1. DevOps Engineer (0.4218)
   Category: Cloud | Level: Advanced
   Skills: docker kubernetes ci cd linux aws automation
   Description: Automate deployment and infrastructure management.
```

## How It Works

1. The script loads `tech_stacks.csv` and normalizes column names.
2. It validates that all required fields exist.
3. It merges the text fields into a single search document per row.
4. It trains a TF-IDF vectorizer on those search documents.
5. The user query is transformed into the same vector space.
6. Cosine similarity is used to rank the closest matches.

## Production Notes

- The script validates missing columns early, which helps catch bad datasets before recommendation time.
- Input text is normalized to improve matching consistency.
- Recommendations are deterministic for the same dataset and query.
- The code is structured so the loader, trainer, and recommender logic can be reused in a web API or service later.

## Troubleshooting

If you see `Dataset not found`, confirm that `tech_stacks.csv` is in the same folder as the script or pass the correct `--csv` path.

If you see import errors for `pandas` or `scikit-learn`, install the dependencies in the same Python environment you are using to run the script.

If no results feel relevant, try using a query that includes role names, tools, or keywords that appear in the dataset, such as `python`, `react`, `aws`, or `machine learning`.

## Suggested Improvements

- Add a small web UI or API endpoint
- Save trained artifacts if the dataset grows larger
- Add more metadata fields to the CSV for stronger matching
- Add automated tests for dataset validation and ranking behavior
