from django.db import models
# Django nun kendi user ini impoort ediyoruz
from django.contrib.auth.models import User 

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=64)

    class Meta:
        verbose_name="Blog Kategori"
        verbose_name_plural="Blog Kategoriler"

    def __str__(self):
        return self.name

class Post(models.Model):
    #id ler ile iliski kurmak icin;
    # CASCADE category yi silince onunla alakali herseyi de sil demek
    #user icin ise once Djangodan import et.Byk harfle
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    # temel field lerimiz asagidakiler.date lerdeki auto larin True olmasi bizim ekstradan cagirmamiza gerek yok demek
    title=models.CharField(max_length=128)
    content=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)


    # class Meta:
    #     verbose_name="Blog Kategori"
    #     verbose_name_plural="Blog Kategoriler"

    # def __str__(self):
    #     return self.name