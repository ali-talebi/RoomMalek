from django.urls import path
from .views import Check_daily



app_name = 'allocate'
urlpatterns = [
    path('', Check_daily.as_view(), name='total_room')
]