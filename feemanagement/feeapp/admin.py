from django.contrib import admin
from .models import State, District,Company,Course,Qualification,Master_data


class CompaniesAdmin(admin.ModelAdmin):
    list_display = ['company_name','address1', 'phone', 'email', 'website']

class StateAdmin(admin.ModelAdmin):
    list_display = ['state']

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['district_name']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'course_code', 'amount']

class MasterAdmin(admin.ModelAdmin):
    list_display = ['name', 'value', 'type']




admin.site.register(State,StateAdmin)
admin.site.register(District,DistrictAdmin)
admin.site.register(Company, CompaniesAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Qualification)
admin.site.register(Master_data, MasterAdmin)





# Register your models here.
