
from django.urls import path
from .views import home,students,teachers

urlpatterns = [
    path('home/', home),
    path("students/", students),
    path("teachers/", teachers),

   
   
]
