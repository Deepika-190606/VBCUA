from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

def generate_pdf(
    student_name,
    topic,
    transcript,
    understanding_score,
    understanding_level,
    fluency_score,
    speech_rate,
    duration,
    filler_words,
    overall_score,
    feedback
):
    # Create reports folder if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    filename = f"reports/{student_name.replace(' ', '_')}_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>Voice Based Concept Understanding Analyser</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Student:</b> {student_name}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Concept:</b> {topic}", styles["BodyText"]))
    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>Transcript</b>", styles["Heading2"]))
    story.append(Paragraph(transcript, styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>Evaluation Results</b>", styles["Heading2"]))

    story.append(Paragraph(f"Understanding Score : {understanding_score:.2f}%", styles["BodyText"]))
    story.append(Paragraph(f"Understanding Level : {understanding_level}", styles["BodyText"]))
    story.append(Paragraph(f"Fluency Score : {fluency_score}/100", styles["BodyText"]))
    story.append(Paragraph(f"Speech Rate : {speech_rate:.1f} WPM", styles["BodyText"]))
    story.append(Paragraph(f"Duration : {duration:.2f} sec", styles["BodyText"]))
    story.append(Paragraph(f"Filler Words : {filler_words}", styles["BodyText"]))
    story.append(Paragraph(f"Overall Score : {overall_score:.2f}%", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["BodyText"]))

    story.append(Paragraph("<b>AI Feedback</b>", styles["Heading2"]))

    for line in feedback:
        story.append(Paragraph(f"• {line}", styles["BodyText"]))

    doc.build(story)

    return filename