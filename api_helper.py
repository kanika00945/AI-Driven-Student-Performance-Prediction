import os
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# Read API Key
api_key = os.getenv("GOOGLE_API_KEY")

# Create Gemini Client
client = genai.Client(api_key=api_key)


def generate_ai_recommendation(
    student_name,
    age,
    studytime,
    failures,
    absences,
    g1,
    g2,
    prediction
):
    prompt = f"""
You are an academic advisor.

Student Name: {student_name}
Age: {age}
Study Time: {studytime}
Failed Subjects: {failures}
Absences: {absences}
Internal Marks (G1): {g1}
Pre Final Marks (G2): {g2}
Predicted Final Grade: {prediction:.2f}/20

Give:
1. Performance Analysis
2. Strengths
3. Weaknesses
4. Study Tips
5. Motivation

Keep the response short and student-friendly.
"""

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("Gemini Error:", e)
        return f"AI Recommendation Error:\n{e}"