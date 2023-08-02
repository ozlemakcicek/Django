from django.db import models

# Create your models here.
# parantrez ici Fieldoptions denilir.Fieldname(benim verdigim) ve Fieldtype(models. dan sonraki alan)
# blank=True : bos birakabilirim gelen veriye gerek yok anlaminda. null=True database kayit etmeye gerek yok demek

class Path(models.Model):
    path_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.path_name}"


class Student(models.Model):
    path = models.ForeignKey(Path, related_name='students', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
# simdi models yazilinca makemigration(modellere gore hazirlik yap migrations altinda 001_init.. dosyasi olustryr) ve migrate(database de ayaga kaldirmak icin.tablo yapar) komutlarini yazacagiz
