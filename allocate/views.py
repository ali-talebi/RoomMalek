from django.shortcuts import render

# Create your views here.

from .models import Allocate_Student_to_Room
from django.views import View


class Check_daily(View) :

    template_name = "check/show_total_room.html"


    def setup(self, request, *args, **kwargs):
        self.total_rooms = Allocate_Student_to_Room.objects.all()
        return super().setup(request, *args, **kwargs)

    def get(self , request )  :
        print(self.total_rooms )
        context = {
            'T_ROOMS' : self.total_rooms ,
        }

        return render(request , self.template_name , context )



