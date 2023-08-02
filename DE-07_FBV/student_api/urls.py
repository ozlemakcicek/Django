from django.urls import path
from .views import home,student_api,student_create,student_delete,student_detail,student_update
# buraya hangi views in adini yazarsan onun bilgilerini getirir.views-old deseydik onu getirirdi

# kendi yazdigimiz view i import et ve path olarak yolunu belirt.#path im student-list olunca student_api yi dondur dedik
# path icindeki ilk ismi burda istedigin sekilde ver
urlpatterns = [
    path("", home ),
    path("student-list",student_api, name='liste'),
    path("student--create",student_create,name="create"),
      #pk--primarykey
    path("student-detail/<int:pk>",student_detail,name="detail"),
    path("student-delete/<int:pk>",student_delete,name="delete"),
    path("student-update/<int:pk>",student_update,name="update"),
  
   
]

# kendi views imizi olusturduk artik eskisi calismaz.url icin de aynisini yapalim