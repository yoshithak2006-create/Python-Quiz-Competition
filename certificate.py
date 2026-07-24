from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from datetime import datetime


def create_certificate(name, score):

    file_name = f"{name}_certificate.pdf"

    c = canvas.Canvas(
        file_name,
        pagesize=A4
    )

    width, height = A4


    # Background border

    c.setStrokeColor(
        HexColor("#1E3A8A")
    )

    c.setLineWidth(5)

    c.rect(
        40,
        40,
        width-80,
        height-80
    )


    # Title

    c.setFont(
        "Helvetica-Bold",
        28
    )

    c.drawCentredString(
        width/2,
        height-150,
        "CERTIFICATE OF ACHIEVEMENT"
    )


    # Subtitle

    c.setFont(
        "Helvetica",
        16
    )

    c.drawCentredString(
        width/2,
        height-210,
        "Python Quiz Competition 2026"
    )


    # Student name

    c.setFont(
        "Helvetica-Bold",
        22
    )

    c.drawCentredString(
        width/2,
        height-300,
        name
    )


    # Score

    c.setFont(
        "Helvetica",
        18
    )

    c.drawCentredString(
        width/2,
        height-360,
        f"Score : {score}/50"
    )


    # Date

    c.setFont(
        "Helvetica",
        14
    )

    c.drawCentredString(
        width/2,
        height-430,
        f"Date : {datetime.now().strftime('%d-%m-%Y')}"
    )


    # Signature

    c.drawString(
        100,
        120,
        "Coordinator"
    )

    c.drawString(
        400,
        120,
        "Organizer"
    )


    c.save()


    return file_name