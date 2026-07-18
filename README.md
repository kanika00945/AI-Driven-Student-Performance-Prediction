# AI-Driven Student Performance Prediction System

A Machine Learning and Generative AI-based web application that predicts student academic performance using academic data. The application integrates the Google Gemini API to generate intelligent performance analysis, personalized recommendations, and a downloadable PDF report.

---

## Overview

This project combines Machine Learning and Generative AI to help evaluate student performance. Users can enter academic details through a Streamlit-based interface, receive prediction results, view AI-generated insights, and download a detailed PDF report.

---

## Key Features

- Machine Learning-based student performance prediction
- Interactive Streamlit web application
- AI-powered performance analysis using Google Gemini API
- Personalized improvement recommendations
- Downloadable PDF report generation
- Clean and user-friendly interface
- Fast prediction using a pre-trained model

---

## Technology Stack

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **Web Framework:** Streamlit
- **Data Processing:** Pandas, NumPy
- **Generative AI:** Google Gemini API
- **PDF Generation:** ReportLab
- **Model Serialization:** Joblib

---

## Project Structure

```text
AI-Driven-Student-Performance-Prediction/
│
├── app.py
├── train_model.py
├── api_helper.py
├── pdf_report.py
├── model.pkl
├── student_data.csv
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/<your-github-username>/AI-Driven-Student-Performance-Prediction.git
```

### Navigate to the project directory

```bash
cd AI-Driven-Student-Performance-Prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### Run the application

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## Machine Learning Workflow

1. Load the student dataset
2. Preprocess the data
3. Train the Machine Learning model
4. Save the trained model
5. Accept user input through the Streamlit interface
6. Predict student performance
7. Generate AI-powered analysis using Gemini
8. Export the prediction report as a PDF

---

## Input Parameters

The prediction model uses academic and study-related information, including:

- Study Hours
- Attendance
- Previous Scores
- Sleep Hours
- Extracurricular Activities
- Sample Papers Practiced

---

## Output

The application provides:

- Predicted Student Performance
- AI-generated Performance Analysis
- Personalized Recommendations
- Downloadable PDF Report

---

## Security

Store your Gemini API key in the `.env` file.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

> **Do not upload your `.env` file or API key to GitHub.**

---

## Author

**Kanika Chauhan**

B.Tech in Computer Science & Engineering (Artificial Intelligence & Machine Learning)

---

## License

This project is developed for educational and learning purposes.
