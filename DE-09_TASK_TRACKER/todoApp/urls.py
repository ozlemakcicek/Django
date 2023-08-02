from django.contrib import admin
from django.urls import path

# from .views import home
from .views import home,todo_list_create,todo_get_delete_update,Todos,TodosRUD

urlpatterns = [
    path('',home),

    #*fbv(function basic view)

    # path('list',todo_list_create ),
    # path('list/<int:pk>',todo_get_delete_update )

#* cbv
    path('todo/',Todos.as_view() ),
    path('todorud/<int:pk>',TodosRUD.as_view() )

]


