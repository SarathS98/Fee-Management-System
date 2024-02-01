
from django.contrib import admin
from django.urls import path
from student.views import generate_pdf

urlpatterns = [
    # Other URL patterns...
    path('generate-pdf/', generate_pdf, name='generate_pdf'),
    path("admin/", admin.site.urls),
]
