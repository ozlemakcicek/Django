from django.urls import path
#* router icin viewset icin lazim
from rest_framework import routers
from .views import (
  home,
  student_api,
  student_create,
  student_delete,
  student_detail,
  student_update,

  #!classViews
  StudentListCreate,
  StudentDetail,

  
  StudentGAV,
  StudentDetailGAV,


  StudentCV,
  StudentDetailCV,

  StudentMVS,
  PathMVS


  )

# viewset icin class  den bir nesne(instance) olusturduk
router=routers.DefaultRouter()
router.register("student", StudentMVS)
router.register("path", PathMVS)
# buraya hangi views in adini yazarsan onun bilgilerini getirir.views-old deseydik onu getirirdi

# kendi yazdigimiz view i import et ve path olarak yolunu belirt.#path im student-list olunca student_api yi dondur dedik
# path icindeki ilk ismi burda istedigin sekilde ver
urlpatterns = [

  #! Function views endpoint
    # path("", home ),
    # path("student-list",student_api, name='liste'),
    # path("student--create",student_create,name="create"),
    #   #pk--primarykey
    # path("student-detail/<int:pk>",student_detail,name="detail"),
    # path("student-delete/<int:pk>",student_delete,name="delete"),
    # path("student-update/<int:pk>",student_update,name="update"),
  


  #! Class views endpoint

#path("student/",StudentListCreate.as_view()),
#path("student-detail/<int:pk>", StudentDetail.as_view())
#int:pk integer primary key

#path("student/",StudentCV.as_view()),
#path("student-detail/<int:pk>", StudentDetailCV.as_view()),
#router in path ini iki sekilde 
#path("",include(router.urls))
]

# kendi views imizi olusturduk artik eskisi calismaz.url icin de aynisini yapalim


#! mevcut urlpatterns e router in kini += ile ekliyoruz.ya da yukarida iceri de ekleyeblrsin path olarak
#! ModelViewSet kullaninca  ve bunu views de asagidaki sekilde Student listemizi alarak yaptigi icin ustteki path leri kapatabiliriz artik.sadece alttaki urlpatterns yeterli
# class StudentMVS(ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


urlpatterns +=router.urls