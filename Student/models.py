from django.db import models

# Create your models here.

class Student_Information(models.Model):
    name = models.CharField(max_length=100 , verbose_name="نام و نام خانوادگی"  )
    student_number = models.CharField(max_length=100 , verbose_name= "شماره دانشجویی"  , default=0 )
    phone     = models.CharField(max_length=11 , verbose_name="شماره همراه"  , default=0)


    def __str__(self):
        return self.name


    class Meta:
        db_table = 'Student_Information'
        verbose_name_plural =  "مشخصات دانشجویان"



