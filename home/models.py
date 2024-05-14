from django.db import models
from django.urls import reverse
# Create your models here.



class Room(models.Model):
    name = models.CharField(max_length=100 , verbose_name= "شماره اتاق" )
    capacity = models.IntegerField(verbose_name= "ظرفیت اتاق"  , default=6 )
    floor = models.IntegerField(verbose_name=  "شماره طبقه" , default= 1 )

    def get_absolute_url(self):
        return reverse("home:detail" , args=[self.id] )




    def __str__(self):
        return self.name


    class Meta:
        db_table = 'Room'
        verbose_name_plural = "اتاق ها خوابگاه"

        ordering = ['name']


