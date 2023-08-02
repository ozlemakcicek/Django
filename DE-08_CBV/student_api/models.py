from django.db import models

class Path(models.Model):
    path_name = models.CharField(max_length=50)
    # students 

    def __str__(self):
        return f"{self.path_name}"

# related_name modeller arasinda baglanti kurar.Path model i parent gibi Student da child gibi.aslinda alt-ust
class Student(models.Model):
    path = models.ForeignKey(Path, related_name='students', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    age = models.IntegerField()
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
# burda bir degisiklik yapinca migrate yapmaya gerek yok.ustte yaparsak makemigration ve migrate i tekrar girmeliyiz