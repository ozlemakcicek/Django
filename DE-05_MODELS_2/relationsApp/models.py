from django.db import models

# Create your models here.
#bir Profile in bir tane Accountu olur.veya tersi.simdi bu ikisini birbirine baglayip bilgileri kullanacagiz.Profile da account=models.OneToOneField(Account,on_delete=models.CASCADE) yapi bu
# CASCADE kullanirsak silinme durumunda primary silinince foreigh de silinsin dedik
class Account(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    email=models.EmailField(null=True)

    #silmek icin ya buraya ya asagiya(Profile model ine) yazariz.ikisi birden olmaz.ya Account dan ya Profile dan silersin.ikisi birbirine baglantili
    #profile=models.OneToOneField(Profile,on_delete==models.CASCADE)

    def __str__(self):
        return self.name



class Profile(models.Model):
    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    about=models.TextField(null=True)   
    phone=models.BigIntegerField(null=True)
    avatar= models.ImageField('userpicture', blank=True, upload_to=('media/' ))

    #TextField ile CharField arasindaki fark;CVharField de max-length yazmak zorundayiz

       #? image kullanıcaksan yapılacaklar
    # 1 - pillow paketini kur              
    #       python -m pip install Pillow
    # 2 - settings.py a ekle     
    #       MEDIA_URL = 'media/
    # 3 - urls.py a ekle
            # from django.conf import settings
            # from django.conf.urls.static import static
            # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    account=models.OneToOneField(Account,on_delete=models.DO_NOTHING)

    # CASCADE      primary silindiginde foreign da silinir
    # set_NULL     null olarak gunceller
    # DO_NOTHING   field oldugu gibi kalir
    # SET_DEFAULT  istenilen bir deger atanir
    # PROTECT      silmeye izin vermez
    



# admin paneldeki ismi degistirmek icin yapariz
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="profile about user"    
        verbose_name_plural="users profile" 

#? terminalde shell e gecip(python manage.py shell diyerek) asagidaki islemleri yapabilirsin.boylece App e yeni veri ekler,istedigini cagirabilirsin.exit diyerek tekrar cikabilirsin
# obj=Profile.objects.all(  tum objeleri getir) 
# obj=Profile.objects.get(name='' )  # olusturuken app i name kullanmistik.icine de hangisini getirmek istersen onu yaz
# obj=Profile.objects.filter(name__startswith='n' )
# obj=Profile.objects.filter(name__contains='n' )
# obj=Profile(name='dzlem',surname='RRTR',phone=789499)   appe girdigimiz basliklarla yeni veri gir sonra
#obj.save() de ve kaydet.gormek icin de yine yukaridaki all() komutunu kullan
# kucuk byk harfe duyarli degil

#bir Accountun birden fazla adresi olabilir
class Adress(models.Model):
    name=models.CharField(max_length=20)
    adress=models.TextField(null=True)
    account=models.ForeignKey(Account,on_delete=models.CASCADE,null=True)

 # account=models.ForeignKey(Account,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Product(models.Model):
    productname=models.CharField(max_length=20)
    account=models.ManyToManyField(Account)


    def __str__(self):
        return self.productname

# class basket(models.Model):
#     account=models.ForeignKey(Account)
#     product=models.ForeignKey(Product)     
