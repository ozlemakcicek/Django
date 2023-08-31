```sh
#! EGER baskasinin reposundan projeyi cekiyorsan once pip install -r requirements.txt yapmalisinki requirements dosyasindaki butun paketleri getirsin ve calsitirsin
#! database icin ise py manage.py makemigrations ve migrete yapmalisin

# 1- calisacagin klasore gir ve terminalde powershell i sec
# 2- python -m venv env
# 3- .\env\Scripts\activate(deactivate diyerek de iptal edip tekrar activate yapabilrisin)  
# 4- pip install djangorestframework.Ve maindeki settings de installed apps icine  #3rd parth apps diyerek 'rest_framework' ekliyoruz
# 5- django-admin startproject main .
# 5i- python manage.py startapp appname
# 6- python manage.py runserver
# 7- pip freeze >requirements.txt
# 8- pip install python-decouple(SECRET_KEY i sifrelemek icin)
# 9- .env dosyasina ana klasore kur.
# 10- main deki settings den SECRET_KEY i al ve .env ye tasi('' ve bosluk olmayacak sekilde) ve SECRET_KEY= diyerek esitle.settingsde de SECRET_KEY=config('SECRET_KEY') yap.

# 11- yine settingsde from decouple import config yaziyoruz import Path in altina.decouple i instalkled apps olarak yazmiyoruz

# 12- terminale history yazarak yazdigin kodlari takip edebilirsin
# 13- .gitignore dosyasi olustur parenta ve internetten django gitignore deyip icerigini copy paste yap.ya da eski derslerden alabilirisn

# 14- (direkt bu projeyi terminalden repoya gonderebilriisn.once disari cikart projeyi sonra kendi terminalinde git init yaz ve initialize olmasini sagla). SONRA stage e alacagiz bunu (git add .) ile.SONRA git commit -m "mesaj yaz"  ile commit birakiyoruz. SONRA git status ile on branch main i gorursek tamamdir.SIMDI repoya push layalim.GITHUB  da yeni bir repo olustruup, adini ver(template bolumu var.tiklayinca bisey gelmiyorsa gidip clonlamak istedigin repoyu sec ve settings den template olarak ekle kutusunu isaretle.artik yeni repodaki template alaninda cikar.Bu ayni seyleri tekrar yukleme demk.template olarak klonla ve yeni repoda kullan demek).SONRA create diyoruz ve bize bir komut satiri verir.brach main de kalacak(main degilse ordaki -M li komutu terminale yaz) ve git remote add li olan satiri terminale onu ekle.ve push lu komutu da al ekle.artik repoya gelmistir

# 15- eger PostgreSQL kullanacaksak once pip install psycopg2 ile yukleyelim.pip freeze >requirements.txt diyerek ekliyoruz

# 16- documentation hazirlamak icin swagger kullanacaksak eger(redom var yine.Shopify.dev den de yine api dokumantasyonlarina bakablrsn), once pip install drf-yasg i yukle.django restframework swagger in kendi dokumantationundan da bakabilrisin installation bolumunden. Yine ordan installed apps kismi icin   'django.contrib.staticfiles',  # required for serving swagger ui's css/js files (ama bu zaten default olarak vardi installed app lerde.silebilirsin) ve 'drf_yasg', yi ekle.SONRA yine dokumanda main url icin olan bolumu alip, main deki herseyi silip oraya yapistir ve projene gore title, description, terms of service ve path lerini duzenleyebilirsin

# 17- IMAGE icin; once Pillow u kurmalisin.py -m pip install Pillow.ve hemen pip freeze >requirements.txt ile ekle sisteme. Settings de STATIC_URL in altina MEDIA_URL = 'media/' ve MEDIA_ROOT=BASE_DIR/"pictures"ekle.main in urls.py ye de  de from django.conf import settings from django.conf.urls.static import static ve if settings.DEBUG:  ve urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) seklinde 3 kodu yaziyoruz
# canlı da seç beğen https://django-storages.readthedocs.io/en/latest/ 










```