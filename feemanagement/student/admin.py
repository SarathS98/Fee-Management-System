# from ast import Name
# from optparse import Values
# from typing import Any
# from urllib import response
# from django.contrib import admin
# from django.db.models.query import QuerySet
# from django.http import HttpResponse
# from django.http.request import HttpRequest
# from django.urls.resolvers import URLPattern
# from reportlab.pdfgen import canvas

# from feemanagement.feeapp.models import Master_data
# from .models import Student,Receipt
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import Table, TableStyle

# from reportlab.lib import colors
# from django.urls import reverse
# from django.utils.html import format_html
# from django.urls import path
# from django.utils.safestring import mark_safe


# class StudentFormAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         if obj.payment_type == 'One Time':
#             obj.payment_type = Master_data.objects.filter(Name='One Time').first().value
#             super().save_model(request, obj, form, change)
#             Receipt.objects.create(Studemt_form=obj, amount=obj.payment_type)
#         elif obj.payment_type == 'Two Time':
#             two_time_record = Master_data.objects.filter(Name='Two Time')
#             values = [record.value for record in two_time_record]
#             obj.payment_type = ', '.join(values)
#             super().save_model(request, obj, form, change)
#             for value in values:
#                 Receipt.objects.create(student_form=obj, amount=value)
#         elif obj.payment_type == 'Three Time':
#             two_time_record = Master_data.objects.filter(Name='Three time')
#             value = [record.value for record in two_time_record]
#             obj.payment_type =', '.join(values)
#             super().save_model(request, obj, form, change)
#             for value in values:
#                 Receipt.objects.create(student_form=obj, amount=value)

#     def view_receipts_link(self, obj):
#         receipt_url = reverse('admin:%s_%s_changelist' % (Receipt._meta.app_label, Receipt._meta.model_name))
#         return format_html('<a href="{}?student_form_id_exact={}">View Receipt</a>', receipt_url, obj.id)
    
#     view_receipts_link.short_description = "Receipt"

#     list_display = ['name','company','state','district','qualification','course','view_receipt_link']



#     class ReceiptAdmin(admin.ModelAdmin):
#         def get_queryset(self, request):
#             qs = super().get_queryset(request)
#             student_id = request.GET.get('student_id_exact')
#             if student_id:
#                 qs = qs.filter(student_id=student_id)
#             return qs


# # def downlod_pdf(self,request, queryset):
# #     Student = self.model.__name__
# #     response = HttpResponse(content_type='application/pdf')
# #     response['Content-Disposition'] = f'attachment; filename={Receipt}.pdf'

# #     pdf = canvas.Canvas(response,pagesizes=letter)
# #     pdf.setTitle('PDF Report')

# #     headers = [field.verbose_name for field in self.model._meta.fields]
# #     data = [headers]

# #     for obj in queryset:
# #         data_row = [str(getattr(obj, field.name)) for field in self.model._meta.fields]
# #         data.append(data_row)

# #         table = Table(data)
# #         table.setStyle(TableStyle(
# #             [
# #                 ('BACKGROUND', (0,0), (-1,0), colors.grey),
# #                 ('GRID', (0,0),(-1,1), 1, colors.black)
# #             ]
# #         ))

# #         canvas_width = 600
# #         canvas_height = 600

# #         table.wrapOn(pdf, canvas_width, canvas_height)
# #         table.drawnOn(pdf, 40, canvas_height - len(data))

# #         pdf.save()
# #         return response
# #     downlod_pdf.short_description = "Download selected items as PDF."


#     def generate_pdf(self, request, receipt_id):
#         receipt = self.get_object(request, receipt_id)
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = f'attachment; filename={receipt.student.name}_receipt.pdf'

#         p = canvas.Canvas(response)
#         p.drawString(100, 750, f'Name: {receipt.student.name}')
#         p.drawString(100, 730, f'Company: {receipt.student.company}')
#         p.drawString(100, 710, f'Qualification: {receipt.student.qualification}')
#         p.drawString(100, 690, f'Course: {receipt.student.course}')
#         p.drawString(100, 670, f'Receipt Number: {receipt.student.amount}')
#         p.showPage()
#         p.save()

# # class StudentAdmin(admin.ModelAdmin):
# #     list_display = ['name', 'company','district', 'qualification']

# #     actions=['download_pdf']

#     def generate_pdf_link(self, obj):
#         pdf_url = reverse('admin:generate_pdf', args=[obj.pk])
#         return format_html('<a href="{}">Generate Pdf</a>',pdf_url)
    
#     generate_pdf_link.allow_tags = True
#     generate_pdf_link.short_description = 'PDF'

#     list_display = ['student_form','amount','generate_pdf_link']

#     def get_urls(self):
#         urls = super().get_urls()
#         custom_urls = [
#             path('generate_pdf/<int:receipt_id>', self.generate_pdf, name='generate_pdf')
#         ]
#         return custom_urls + urls



#     admin.site.register(Student,StudentFormAdmin)
#     admin.site.register(Receipt,ReceiptAdmin)







from django.contrib import admin
from django.http import HttpResponse
from reportlab.pdfgen import canvas

from .models import Student, Receipt

class ReceiptAdmin(admin.ModelAdmin):
    def generate_receipt_pdf(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="receipts.pdf"'

        p = canvas.Canvas(response)
        for receipt in queryset:
            p.drawString(100, 750, f'Name: {receipt.student.name}')
            p.drawString(100, 730, f'Company: {receipt.student.company}')
            p.drawString(100, 710, f'Qualification: {receipt.student.qualification}')
            p.drawString(100, 690, f'Course: {receipt.student.course}')
            p.drawString(100, 670, f'Receipt Number: {receipt.amount}')
            p.showPage()
        p.save()
        return response

    generate_receipt_pdf.short_description = 'Download PDF for selected receipts'

    actions = ['generate_receipt_pdf']
    list_display = ['student', 'amount', 'active']

admin.site.register(Student)
admin.site.register(Receipt, ReceiptAdmin)
