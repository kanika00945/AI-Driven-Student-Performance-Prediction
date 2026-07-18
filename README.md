# AI-Driven Student Performance Prediction System

An AI-powered web application that predicts a student's final academic performance using Machine Learning. The system uses a Random Forest Regression model to estimate the final grade and integrates Google's Gemini API to generate personalized academic recommendations. Users can also download a detailed PDF performance report.

---

## Overview

The AI-Driven Student Performance Prediction System is designed to help evaluate a student's academic performance using Machine Learning and Generative AI. Based on the student's academic information, the application predicts the expected final grade (G3), provides AI-powered study recommendations, classifies the student's performance level, and generates a downloadable PDF report.

---

## Features

- Predicts the student's final academic grade using Machine Learning.
- Uses the Random Forest Regression algorithm for prediction.
- Interactive and user-friendly Streamlit web application.
- AI-generated academic analysis and study recommendations using Google Gemini.
- Classifies student performance (Excellent, Good, Average, Poor).
- Generates a professional PDF performance report.
- Modern and responsive user interface.

---

## Technology Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Google Gemini API
- ReportLab
- Python-dotenv

---

## Project Structure

```text
AI-Driven-Student-Performance-Prediction/
│
├── app.py
├── api_helper.py
├── pdf_report.py
├── train_model.py
├── model.pkl
├── student_data.csv
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/kanika00945/AI-Driven-Student-Performance-Prediction.git
```

### Navigate to the project directory

```bash
cd AI-Driven-Student-Performance-Prediction
```

### Install the required packages

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### Run the application

```bash
streamlit run app.py
```

---

## Machine Learning Model

**Algorithm Used**

- Random Forest Regressor

### Input Features

### Input Features

- Student Name
- Age
- Study Time
- Previous Failed Subjects
- Absences
- Internal Assessment (G1)
- External Assessment (G2)

### Output

- Predicted Final Grade (G3)
- Student Performance Level
- AI-generated Academic Analysis
- Personalized Study Recommendations
- Downloadable PDF Report

---

## Application Workflow

1. Enter the student's personal information.
2. Provide academic details.
3. Click **Predict Performance**.
4. View the predicted final grade.
5. Read the AI-generated academic recommendations.
6. Download the PDF performance report.

---

## Security

Store your Google Gemini API key in a `.env` file.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

The `.env` file is excluded from Git using `.gitignore` and should never be uploaded to GitHub.

---

## Future Improvements

- Support multiple Machine Learning models.
- Performance visualization using charts.
- Student prediction history.
- Model comparison.
- Multi-user support.

---

## Author

**Kanika Chauhan**

Bachelor of Technology (Computer Science & Engineering – Artificial Intelligence & Machine Learning)

---

## Disclaimer

This project was developed for educational, internship, and portfolio purposes.