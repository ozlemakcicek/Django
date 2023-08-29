from django.urls import path,include
from .views import home,body,studentView,student_addView,StudentAddView
urlpatterns = [
    path('', body),
    path('home', home),
    path('student', studentView, name='list'),  # name ler uniq olmali.ya path adi ya da name ile ulasilabilir verilere
    # forms
    #fbv
    path('add', student_addView),
    #cbv
    path('add', StudentAddView.as_view(), name='add')
]
