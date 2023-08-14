

* https://docs.docker.com/get-started/docker_cheatsheet.pdf

```sh

    $ docker --version    #ile dockerin calisip calismadigini kontrol edebiliriz
    $ docker version # Detaylı versiyon bilgisi.

    $ docker info  # bilgi almak icin

    $ docker --help           #yazilmasi gereken komutlari gosterir
    $ docker help
    $ docker command --help       # komuta gore yardim

    $ docker search <imagename> # dockerhub'da ara.bunu kendi sayfasindan da arayabilirisn daha rahat olur





# Image Build:
    $ docker build .
    $ docker build . --tag <imagename> # lowercase
    $ docker build . -t <imagename> # lowercase
    # Image build et ve image'a isim:sürüm ver:
    $ docker build . -t <imagename:version>
    $ docker build . -t <imagename:version> --no-cache



    #Image'leri listeleme

    $ docker image ls
    $ docker images

    # Image Silme:
    $ docker rmi <imagename:version>   #silerken versionunu da yazmaliyiz , yoksa  id sinin birkac ogesini yazarak sileblrz

    # Image TAG ekle/degistir: (copy/paste)  eskiyi silmez
    $ docker tag <newimagename>



    #Tümünü sil:
    $ docker images prune -a -f # Aktif olmayanlari sil.Cache de silinir


    # Container Run: olusturulan klasorler skistirilmis halde.bunu container haline yanmi zip ten cikartip kullanilir hale getirmeye calisdacagiz
    $ docker run <imagename>
    $ docker container ls -a  # butun aktiv passiv containerlari goster 
    $ docker run --name <containername> <imagename>

    #Container listele:
    $ docker container ls # Aktif olanlari siralar
    $ docker ps   # bu da container icin listeleme demek
    $ docker ps -a

    #Container start/stop
    $ docker start|stop <containername>

    # Container sil:
    $ docker rm <containername>
    $ docker rm <containername> -f

    # Tümünü sil
    $ docker container prune -f   # Aktif olmayanlari sil.Cache de silinir



    # Interaktif Mod:
    $ docker run -it <imagename> sh   # shelle gecisi saglar

    #ls ile butun dosyalari gorursun. cd .. ile ana dosyaya gecersin.ls /bin deyince ne nerde ana klasorde gorursun.exit ile cikarsin

```


