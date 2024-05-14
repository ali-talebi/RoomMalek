from django.shortcuts import render
from .models import Room
from django.views import View
# Create your views here.



class RoomView_detail(View):

    template_name = "check/show_detail_room.html"

    def setup(self, request, *args, **kwargs):
        self.room = Room.objects.get(id = kwargs['id'])
        return  super().setup(request, *args, **kwargs)


    def get(self ,request, id ):
        context = {
            'room' : self.room
        }
        return render(request , self.template_name , context )


