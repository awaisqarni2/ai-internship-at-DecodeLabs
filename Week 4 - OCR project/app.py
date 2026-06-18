import os
import cv2
import pytesseract

from utils.preprocess import preprocess_image
from utils.ocr_engine import extract_text

# Windows users only
# Uncomment and update path if needed

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

IMAGE_PATH = "images/sample.png"

def main():

    print("\n========== AI OCR SYSTEM ==========\n")

    if not os.path.exists(IMAGE_PATH):
        print("Image not found.")
        return

    processed = preprocess_image(IMAGE_PATH)

    text = extract_text(processed)

    print("Detected Text:\n")
    print(text)

    os.makedirs("output", exist_ok=True)

    with open("output/extracted.txt", "w", encoding="utf-8") as file:
        file.write(text)

    cv2.imshow("Processed Image", processed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("\nOutput saved successfully.")

if __name__ == "__main__":
    main()