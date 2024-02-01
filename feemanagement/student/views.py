from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Receipt

def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="receipt_details.pdf"'

    # Retrieve data from the Receipt model
    receipts = Receipt.objects.all()

    # Create a PDF document
    pdf = canvas.Canvas(response)

    # Write details to the PDF
    y_coordinate = 800  # Initial y-coordinate for text
    for receipt in receipts:
        student_name = receipt.student.name
        amount = receipt.amount
        

        pdf.drawString(100, y_coordinate, f"Student Name: {student_name}")
        pdf.drawString(100, y_coordinate - 20, f"Amount: {amount}")
        

        y_coordinate -= 60  # Adjust y-coordinate for the next receipt

    # Save the PDF document
    pdf.save()
    return response


