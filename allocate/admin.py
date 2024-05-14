from django.contrib import admin
from .models import Allocate_Student_to_Room

# Register your models here.

@admin.register(Allocate_Student_to_Room)
class Allocate_Student_to_RoomAdmin(admin.ModelAdmin):

    list_display = ('student', 'room' , 'show_date' )
    list_filter = ('room'  , )


    def show_date(self, obj):
        return obj.date.strftime("%Y-%m-%d ")