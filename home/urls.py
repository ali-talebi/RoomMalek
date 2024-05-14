from django.urls import path
from .views import RoomView_detail


app_name = 'home'
urlpatterns = [
    path('detail/<int:id>/',  RoomView_detail.as_view(), name='detail' )
]