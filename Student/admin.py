from django.contrib import admin
from .models import Student_Information
# Register your models here.


@admin.register(Student_Information)
class Student_InformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_number', 'phone',  )
    search_fields = ('name' , 'student_number', 'phone' )



