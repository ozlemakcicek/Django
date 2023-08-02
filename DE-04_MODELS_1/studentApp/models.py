from django.db import models

# Create your models here.

    # model olusturdu isen ;
    # önce python manage.py makemigrations
    # sonra python manage.py migrate yap teminalde

class Student(models.Model):

    COHORTS=(
        ("FS", "Fullstack"),
       ( "DS","DataScience"),
        ("AWS","AWS Devops"),
    )

    number=models.IntegerField()
    first_name=models.CharField(max_length=30) #charfield da maxlength zorunlu
    last_name=models.CharField(max_length=40)
    comment=models.TextField(null=True)
    register_date=models.DateTimeField(auto_now_add=True, null=True)
    updated_date=models.DateTimeField(auto_now=True, null=True)
    is_active=models.BooleanField(default=True)
    cohort=models.CharField(max_length=3,choices=COHORTS,default="FS")
    email=models.EmailField(null=True)

 # burda tanimlaynca almaz.once yukarida yazmaliyiz 
    # CHOIS=(
    #     ("FS", "Fullstack"),
    #    ( "DS","DataScience"),
    #     ("AWS","AWS Devops"),
    #     )

   

        # admin panel de ki verdigimiz tanimlamalari dondurmek icin ;
    def __str__(self):
        return f"{self.first_name}  {self.last_name}"


## Meta
    class Meta:
        ordering=["-first_name"]
        verbose_name_plural="Student list"




