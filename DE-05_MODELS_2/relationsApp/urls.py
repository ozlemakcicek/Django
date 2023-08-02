

from django.urls import path,include
# from.views import * # herseyi demek cok tavsiye edilmez

from.views import  home

urlpatterns = [
   
    path('', home),
]