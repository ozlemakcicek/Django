from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
#!inherit etsin asagidakiler diye FixFields olusturalim.
class FixFields(models.Model):
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
#!yalniz migrate yapinca yeni bir field acar.bunu istemezsek asagiya class Meta  abstract=True yapariz
    class Meta:
        abstract=True


   


class Category(models.Model):
    name=models.CharField(max_length=30)


    def __str__(self):
        return self.name




class Brand(models.Model):
    name=models.CharField(max_length=30)
    image=models.TextField()   # imageField kullansaydik pillow u yuklememiz lazimdi.textField de kullanialablr


    def __str__(self):
        return self.name


class Product(FixFields):
    name=models.CharField(max_length=30)
    category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products')
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE, related_name='b_products')
    stock=models.SmallIntegerField(blank=True,default=0)
    
    


    def __str__(self):
        return self.name



class Firm(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    adress=models.CharField(max_length=30)
    image=models.TextField()   


    def __str__(self):
        return self.name




class Purchases(FixFields):
    #normalde CASCADE yerine null daha mantikli moels.SET_NULL 
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firm=models.ForeignKey(Firm,on_delete=models.CASCADE,related_name='purchases')
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE, related_name='b_purchases')
    product=models.ForeignKey(Brand,on_delete=models.CASCADE, related_name='p_products')
    quantity=models.SmallIntegerField()
    price=models.DecimalField(max_digits=8,validators=[MinValueValidator(0)],decimal_places=2)
    price_total=models.DecimalField(max_digits=8,validators=[MinValueValidator(0)],decimal_places=2)


    def __str__(self):
        return  f"({self.user}-{self.product}-{self.quantity})" 



class Sales(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE, related_name='b_sales')
    product=models.ForeignKey(Brand,on_delete=models.CASCADE, related_name='p_sales')
    quantity=models.SmallIntegerField()
    price=models.DecimalField(max_digits=8,validators=[MinValueValidator(0)],decimal_places=2)
    price_total=models.DecimalField(max_digits=8,validators=[MinValueValidator(0)],decimal_places=2)


    def __str__(self):
        return  f"({self.user}-{self.product}-{self.quantity})" 