from reportlab.pdfgen import canvas

def create_certificate(name, score):
    filename = f"{name}_Certificate.pdf"

    c = canvas.Canvas(filename)

    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(300, 780, "PYTHON QUIZ COMPETITION")

    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(300, 730, "CERTIFICATE OF ACHIEVEMENT")

    c.setFont("Helvetica", 14)
    c.drawCentredString(
        300,
        680,
        f"This is to certify that {name}"
    )

    c.drawCentredString(
        300,
        650,
        "has successfully completed"
    )

    c.drawCentredString(
        300,
        620,
        "Python Quiz Competition"
    )

    c.drawCentredString(
        300,
        590,
        f"Score : {score}/50"
    )

    c.drawCentredString(
        300,
        540,
        "Congratulations!"
    )

    c.save()

    return filename