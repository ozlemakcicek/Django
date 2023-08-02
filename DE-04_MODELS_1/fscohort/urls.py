
from django.urls import path
from .views import fswelcome

urlpatterns = [
   
    # artik burda path belirtmeye gerek yok sadece fonksiyon ismini yaziyoruz.ustte de butun views lerden anlaminda .views diyoruz
    path("",fswelcome),
    
]