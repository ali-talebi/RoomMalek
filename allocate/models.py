from django.db import models
from Student.models import Student_Information
from home.models import Room
from django.utils import timezone
from django_jalali.db import models as jalali_models
# Create your models here.



class Allocate_Student_to_Room(models.Model):

    student = models.ForeignKey(Student_Information , unique=True  , verbose_name='دانشجو', related_name = 'student_allocated' , on_delete=models.SET_NULL, null=True )
    room = models.ForeignKey(Room , verbose_name='اتاق' , related_name = 'room_allocated' ,  on_delete=models.SET_NULL , null=True  )
    date = jalali_models.jDateTimeField(default=timezone.now  )


    def __str__(self):
        return f'{self.student} -> {self.room} '



    class Meta :
        db_table = 'Allocate_Student_to_Room'
        verbose_name_plural  = 'انتساب دانشجو به اتاق '




