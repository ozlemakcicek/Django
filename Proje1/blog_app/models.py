from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

#* asagidaki alan admin panelde gorebilmek icin lazim.eger yazmazsak bize object diye dondiurur

def __str__(self):
        return f"{self.name}"





class Post(models.Model):
  
    user = models.ForeignKey(User, related_name='post',on_delete=models.CASCADE) # django nun kendi user modeli var.onun ile biz burda kendi modelimizi iliskilendiriyoruz.Foreighnkey id icin lazim
    category = models.ForeignKey(Category,related_name='post', on_delete=models.CASCADE) # bu da bizim olusturdugumuz category model i.onun icinde id istiyordu canli da
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    created_date=models.DateTimeField(auto_now_add=True,blank=True,null=True) #! Ilk task eklenirken eklenir sadece
    updated_date=models.DateTimeField(auto_now=True)  #! her islem degisikliginde tarih ekler
    # created_date ile updated_date i browserda eklememize gerek yok cunku auto_now_add dedik burda

    def __str__(self):
        return f" {self.title} "
