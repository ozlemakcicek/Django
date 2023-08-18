from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE)
  image=models.ImageField(upload_to="pictures",default="/pictures/avatar.png" )
  # image kullaniyorsan pip install Pillow
  about=models.TextField(blank=True, null=True)

  def __str__(self):
      return f"{self.user.username}"
# Create your models here.















#!EGER Django nun kendi user modelini kullanmayacaksaniz asagidaki gibi abstructuserda inherit edip kendi modelinizi olusturablrsnz
#? settings.py ye yeni modeli bildirin
# from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# from datetime import date
# class MyUser(AbstractUser):
#   username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
#   email = models.EmailField(('email address'), unique = True)
#   native_name = models.CharField(max_length = 5)
#   phone_no = models.CharField(max_length = 10)
#   USERNAME_FIELD = 'email'
#   REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
#   def __str__(self):
#       return "{}".format(self.email)


    
