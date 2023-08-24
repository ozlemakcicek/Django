from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Department(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=30)  
    def __str__(self):
        return self.name
GENDER=(
    ("M","Male"),
    ("F","Female"),
    ("O","Other"),
    ("X","Prefer not to say"),
)
TITLE=(
    (1,"Manager"),
    (2,"Team Lead"),
    (3,"Developer"),
    (4,"Junior"),
)

class Personnel(models.Model):

    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,related_name="personnels")
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    gender=models.CharField(max_length=1,choices=GENDER)
    title=models.IntegerField(choices=TITLE)
    salary=models.IntegerField(default=1000)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    start_date=models.DateTimeField()
    
    def __str__(self):
        return  f"{self.title} {self.first_name}"

