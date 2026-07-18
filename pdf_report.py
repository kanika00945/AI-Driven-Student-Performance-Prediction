from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(
    filename,
    student_name,
    age,
    studytime,
    failures,
    absences,
    g1,
    g2,
    prediction,
    performance,
    ai_response
):

    styles = getSampleStyleSheet()

    pdf = SimpleDocTemplate(filename)

    elements = []

    elements.append(Paragraph("<b>AI-Driven Student Performance Prediction Report</b>", styles["Title"]))

    elements.append(Paragraph("<br/>", styles["Normal"]))

    elements.append(Paragraph(f"<b>Student Name:</b> {student_name}", styles["Normal"]))
    elements.append(Paragraph(f"<b>Age:</b> {age}", styles["Normal"]))
    elements.append(Paragraph(f"<b>Study Hours:</b> {studytime}", styles["Normal"]))
    elements.append(Paragraph(f"<b>Failed Subjects:</b> {failures}", styles["Normal"]))
    elements.append(Paragraph(f"<b>Absences:</b> {absences}", styles["Normal"]))
    elements.append(Paragraph(f"<b>Mid-Term Marks:</b> {g1}", styles["Normal"]))
    elements.append(Paragraph(f"<b>Pre-Final Marks:</b> {g2}", styles["Normal"]))

    elements.append(Paragraph("<br/>", styles["Normal"]))

    elements.append(Paragraph(f"<b>Predicted Final Grade:</b> {prediction:.2f}/20", styles["Heading2"]))

    elements.append(Paragraph(f"<b>Performance:</b> {performance}", styles["Heading2"]))

    elements.append(Paragraph("<br/>", styles["Normal"]))

    elements.append(Paragraph("<b>AI Analysis & Recommendations</b>", styles["Heading2"]))

    elements.append(Paragraph(ai_response.replace("\n","<br/>"), styles["BodyText"]))

    pdf.build(elements)
    