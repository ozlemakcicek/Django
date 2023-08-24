from django.urls import path,include
from .views import PersonnelView,DepartmentView,Personnel_GPD_View,DepartmentPersonnelView

urlpatterns = [
    path('department/',DepartmentView.as_view()),
    path('personnel/',PersonnelView.as_view()),
    path('personnel/<int:pk>',Personnel_GPD_View.as_view()),
    path("department/<str:department>/", DepartmentPersonnelView.as_view()),


    
]