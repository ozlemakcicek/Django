
#! CBV :Class Basic Views
#! FBV :function Basic Views
from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#!######## Apiviews icin
from rest_framework.views import APIView
#!######## Generic APIView icin
from rest_framework.generics import GenericAPIView, mixins,ListCreateAPIView,RetrieveDestroyAPIView

##! ViewSet icin
from rest_framework.viewsets import ModelViewSet

##!action icin
from rest_framework.decorators import action

#* Create your views here.


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
            

#detail istyrsak.. DELETE,UPDATE ve DETAIL icin id ye yani pk ya ihtiyac var

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



  # delete da serializer a gerek yok  
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

        


       return Response(message) 
    # is_valid degilse
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#!###################################################################
#! Api Views  : yukaridaki yazimin iki satirda yazimi.yukaridaki get ve post daki islemlerin aynisini getirip kopyaliyioruz.orda ayri ayri funct.seklinde yazildi burda toplu class icinde yazdik.boylece ayri ayri endpoint degilde get ve post icin tek bir endpoint yaptik.bu daha clean cod

#? asagidaki sekilde ayni alanda post ve get beraber ve delete,put ve patch de gozukur.

class StudentListCreate(APIView):
    def get(self,request):
        students=Student.objects.all()  
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data) # JSON formatinda

    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                
            message={"message":"Successfully Created"}
            return Response(message,status=status.HTTP_201_CREATED)
           
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    
    def get_obj(self, pk):
        return get_object_or_404(Student, pk=pk)

    def get(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(data=request.data, instance=student)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def patch(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(data=request.data, instance=student, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_obj(pk)
        student.delete()
        data = {
            'message': 'Student succesfully deleted.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


#!yeni bir views olusturmak istersek ustteki yapinin aynisini al ve sadece view in ismini ve serializer daki isimleri degistir(student)

#*eger inherit ederek yapmak istersek; yarim kaldi video dan bak
#class newStudent

#?? Generic APIView and Mixins 

#*GenericAPIView: asil isi yapar
""" One of the key benefits of class-based views is the way they allow you to compose bits of reusable behavior. REST framework takes advantage of this by providing a number of pre-built views that provide for commonly used patterns.

GenericAPIView class extends REST framework's APIView class, adding commonly required behavior for standard list and detail views. Some Basic Attributes and Methods. """


#*mixins : kullanacagimiz islem
""" The mixin classes provide the actions that are used to provide the basic view behavior. Note that the mixin classes provide action methods rather than defining the handler methods, such as .get() and .post(), directly. This allows for more flexible composition of behavior. Tek başlarına bir işlem yapamazlar. GenericAPIView ile anlamlı oluyor """

#*import ettigimiz modellleri kullanip  mixins yazacagiz.StudentSerializerDefinition icin strg+solClick yap mausdan

class StudentGAV( mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):

    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentDetailGAV(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# bunlari da en ustteki StudentGAV dan inherit alarak yazabiliriz.ordaki get ve post islemlerinin aynisini yap demek.ama bu modeller olmadigi icin calismaz yorumda gostermek icin kalabilir

# class MyProductListCreateView(StudentGAV):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# class MyPathListCreateView(StudentGAV):
#     queryset = Path.objects.all()
#     serializer_class = PathSerializer



#! Concrete View Classes.

# *ListCreateAPIView ile get-Post  RetrieveDestroyAPIView ile de detail,delete,put yapiyor.sadece bu iki satir yetiyor


class StudentCV(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailCV(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


##! ViewSets

# bunlarda router yapisi kullaniliyor urls.py de

class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentMVS(ModelViewSet):

    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    
    @action(detail=False, methods=["GET"])
    def student_count(self, request):
        count  = {
            "student-count" : self.queryset.count(),
        }
        return Response(count)


# viewsetlerde ozgu  action var 
class PathMVS(ModelViewSet):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

    @action(detail=True)
    def student_names(self, request, pk=None):
        path = self.get_object()
        students = path.students.all()
        return Response([i.first_name for i in students])









  

        