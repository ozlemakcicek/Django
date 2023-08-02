from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


def home(request):
    return HttpResponse('<h1>API Page</h1>')

# kendi view imizi yaziyoruz
#http methods
# GET     veri getir
# POST    create
# DELETE  veri sil
# PUT     veri degistir.tamamini degistirir
# PATCH   parcali sekilde veri degistirir
@api_view(["GET"])
def  student_api(request):
    students=Student.objects.all()  # veri tipi queryset.bunu pythonun diline cevirecegiz Serialize islemi ile
    serializer=StudentSerializer(students,many=True)
    return Response(serializer.data) # JSON formatinda
    # simdi bunu urls de kullanalim

@api_view(["POST"])
def student_create(request):
    #kontrol etmek icin veri geliyormu diye asagidaki iki islemi yapip rest frameworkda bir veri püost edersen burda teminale duserse tamamdir
    # print(request.data)
    # return Response("deneme")

   # GET deki serializeri al ama burda data diye birseye aktarmamizi istiyor donen sonucu
        serializer=StudentSerializer(data=request.data)
        # eger gelen veri benim modelime  uygunsa kaydet diyoruz ve bir message yayinlamasini istiyoruz.key value seklinde mesaaage i yaz.mesaage status u da yazablrz
        if serializer.is_valid():
            serializer.save()
            message={"message":"Successfully Created"}
            return Response(message,status=status.HTTP_201_CREATED)
            #is_valid degilse uyusmuyorsa icin basina else yazmaya gerek kalmadan bu sekilde yzblrz
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        # calismasi icin yine urls e ekle import ve path seklinde
            

#detail istyrsak
@api_view(["GET"])
def  student_detail(request,pk):
# seri birsey yok tek bir obje ile alakali islem yapiliyor
    #* student=Student.objects.get(id=pk) 
    # # asagidaki ile ayni islem yukaridaki
    student=get_object_or_404(Student, pk=pk)
    serializer=StudentSerializer(student)
    message={"Successfully "}
    data={}
    data["message"]=message
    data["data"]=serializer.data

    return Response(data) 



    
@api_view(["DELETE"])
def  student_delete(request,pk):
# seri birsey yok tek bir obje ile alakali islem yapiliyor
    #* student=Student.objects.get(id=pk) 
    # # asagidaki ile ayni islem yukaridaki
    student=get_object_or_404(Student, pk=pk)
    student.delete()
    message={"message":"Successfully Deleted"}

    return Response(message) 




#! PUT islemleri PATCH ile hemen hemen ayni.o yuzden ayni yere yazip lazim olani acabiliriz
# @api_view(["PUT"])
# def  student_update(request,pk):

#     student=get_object_or_404(Student, pk=pk)
#     # serialize edilmeli.post ile put arasindaki fark instance kismi.pk ile de belli bir nesneyi belirtiyoruz
#     serializer=StudentSerializer(instance=student,data=request.data)
#     if serializer.is_valid():
#         serializer.save()

#         message={"message":"Successfully Updated"}

#         return Response(message) 
#     # is_valid degilse
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
# @api_view(["PATCH"])
def  student_update(request,pk):

    student=get_object_or_404(Student, pk=pk)
    #*PUT yapacaksan asagidaki serialize i calistir
     # serialize edilmeli.post ile put arasindaki fark instance kismi.pk ile de belli bir nesneyi belirtiyoruz
    serializer=StudentSerializer(instance=student,data=request.data)
     
     #*PATCH yapacaksan asagidfaki serialize i calistir
    # serialize edilmeli.patch ile put arasindaki fark partical kismi.pk ile de belli bir nesneyi belirtiyoruz
    #?serializer=StudentSerializer(instance=student,data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()

        message={"message":"Successfully Updated"}

        return Response(message) 
    # is_valid degilse
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
