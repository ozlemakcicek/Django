* https://docs.docker.com/get-started/docker_cheatsheet.pdf

```sh

    $ docker --version
    $ docker version # Detaylı versiyon bilgisi.

    $ docker info

    $ docker --help
    $ docker help
    $ docker command --help

    $ docker search <imagename> # dockerhub'da ara.

```

```sh

    # Image Build:
    $ docker build .
    $ docker build . --tag <imagename> # lowercase
    $ docker build . -t <imagename> # lowercase
    # Image build et ve image'a isim:sürüm ver:
    $ docker build . -t <imagename:version>
    $ docker build . -t <imagename:version> --no-cache

    # Image'leri listele:
    $ docker image ls
    $ docker images
    # Image Silme:
    $ docker rmi <imagename:version> # or imageid
    $ docker rmi <imagename:version> -f
    # Image TAG ekle/değiştir: (copy/paste)
    $ docker tag <oldimagename> <newimagename>
    # Tümünü Sil:
    $ docker image prune -a -f # Aktif olmayanları sil. Cache'da silinir.

    # Container Run:
    $ docker run <imagename>
    $ docker run --name <containername> <imagename>

    # Container listele:
    $ docker container ls # Aktif
    $ docker ps # Aktif
    $ docker container ls -a # Tümü
    $ docker ps -a # Tümü
    # Container start/stop:
    $ docker start|stop <containername>
    # Container sil:
    $ docker rm <containername>
    $ docker rm <containername> -f
    # Tümünü Sil:
    $ docker container prune -f # Aktif olmayanları sil. Cache'da silinir.

    # Interaktif Mod:
    $ docker run -it <imagename> sh
    # Çıkış:
    $ exit

```

```sh

# Komple temizlik:
$ docker system prune -a -f


# DOCKERHUB
$ docker login -u <username> -p <password>
$ docker login   # Autologin
$ docker tag <oldname> <username/newname>  
$ docker push <username/>newname>  # Upload to DockerHub

```

```sh
# DOCKER COMPOSE
# docker-compose.yml
# docker-compose --version
$ docker-compose up
$ docker-compose up -d  # deamon mode: arka planda calisir
$ docker-compose down  # Compose kapat, container sil
$ docker-compose down -v # compose tumunu kapat



Bonus: SuperMario:
    $ docker run -d -p 8600:8080 bharathshetty4/supermario
    # open http://localhost:8600







```