# AI OCR Recognition System using OpenCV & Tesseract

An AI-powered OCR (Optical Character Recognition) system built using Python, OpenCV, and Tesseract OCR that extracts readable text from images using computer vision and image preprocessing techniques.

---

# 📌 Project Overview

This project was developed as part of **Artificial Intelligence Project 4**.

The system performs:

* Image preprocessing
* Text recognition from images
* OCR extraction using AI models
* Output generation into text files

The project demonstrates how pre-trained AI models can be integrated into real-world applications using Python and Computer Vision.

---

# 📄 Project Requirement PDF

Project requirement document included in current directory:

```bash
Artificial Intelligence Project 4.pdf
```

This PDF contains:

* Project objectives
* AI recognition requirements
* OCR/Object Detection guidelines
* Submission instructions
* Recommended technologies

---

# 🚀 Features

✅ OCR Text Recognition
✅ Image Preprocessing
✅ Noise Removal
✅ Thresholding
✅ Text Extraction from Images
✅ Save Output to File
✅ Production-Ready Folder Structure
✅ Beginner Friendly AI Project
✅ OpenCV Integration
✅ Tesseract OCR Integration

---

# 🧠 Technologies Used

| Category             | Technology    |
| -------------------- | ------------- |
| Programming Language | Python        |
| Computer Vision      | OpenCV        |
| OCR Engine           | Tesseract OCR |
| Image Processing     | NumPy         |
| OCR Wrapper          | pytesseract   |

---

# 📂 Project Structure

```bash
project4-ocr/
│
├── app.py
├── requirements.txt
├── README.md
├── Artificial Intelligence Project 4.pdf
│
├── images/
│   └── sample.png
│
├── output/
│   └── extracted.txt
│
└── utils/
    ├── preprocess.py
    └── ocr_engine.py
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/project4-ocr.git
cd project4-ocr
```

---

## 2️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Install Tesseract OCR

## Windows

Download and install:

https://github.com/UB-Mannheim/tesseract/wiki

After installation, update path inside `app.py`:

```python
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
```

---

# ▶️ How To Run

Place your image inside:

```bash
images/
```

Example:

```bash
images/sample.png
```

Then run:

```bash
python app.py
```

---

# 🖼️ Example Workflow

## Input

Image containing text:

* Notes
* Invoice
* Book page
* Printed document

↓

## Processing

* Grayscale conversion
* Gaussian blur
* Thresholding
* OCR extraction

↓

## Output

```txt
Artificial Intelligence
Project 4
Industrial Training Kit
```

Saved automatically into:

```bash
output/extracted.txt
```

---

# 🧪 Image Preprocessing Steps

This project applies:

## 1. Grayscale Conversion

Simplifies image data for OCR.

## 2. Gaussian Blur

Reduces image noise.

## 3. Thresholding

Converts image into black & white for better text recognition.

These preprocessing techniques significantly improve OCR accuracy.

---

# 📜 Requirements

Install required packages:

```txt
opencv-python
pytesseract
numpy
Pillow
```

---

# 📌 Future Improvements

Possible upgrades:

* Real-time webcam OCR
* PDF OCR extraction
* Handwritten text recognition
* Streamlit web dashboard
* Translation system
* AI document scanner

---

# 🎯 Learning Outcomes

By completing this project you will learn:

* Computer Vision basics
* OCR systems
* AI model integration
* Image preprocessing
* OpenCV fundamentals
* Real-world AI workflow

---

# 💼 Resume Description

Built an AI-powered OCR Recognition System using Python, OpenCV, and Tesseract OCR capable of extracting machine-readable text from images using preprocessing and computer vision techniques.

---

# 👨‍💻 Author

## Awais Qarni

AI & Full Stack Developer
Passionate about AI Engineering, Computer Vision, and Backend Development.

---

# 🔍 SEO Keywords

awaisqarni
awaisai
awaisqarniai
AI OCR System
Python OCR Project
OpenCV OCR
Tesseract OCR Python
Computer Vision Project
Artificial Intelligence Project 4
OCR Recognition System
AI Text Detection
Python AI Projects
AI Internship Projects
DecodeLabs AI Project
Machine Learning OCR
Deep Learning OCR
Image Recognition System
AI Developer Pakistan
AI Engineer Portfolio
Computer Vision using Python

---

# ⭐ License

This project is for educational and learning purposes.
