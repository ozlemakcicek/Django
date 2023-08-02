
from django.urls import path
from .views import dswel

urlpatterns = [
   
   # artik burda path belirtmeye gerek yok sadece fonksiyon ismini yaziyoruz
    path("",dswel),
    
]