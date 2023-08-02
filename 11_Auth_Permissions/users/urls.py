
from django.urls import path, include
from .views import RegisterView,logout_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", obtain_auth_token),
    path("logout/", logout_view),
]   
