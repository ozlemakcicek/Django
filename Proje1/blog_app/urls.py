
from django.urls import path

from .views import home,category,post

urlpatterns = [
    
   path("", home),
   path("category/", category),
   path("post/", post)
   
]
