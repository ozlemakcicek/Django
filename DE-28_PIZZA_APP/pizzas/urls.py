from django.urls import path,include
from .views import home,pizzas,order,my_orders

urlpatterns = [
    path('', home, name='home'),
    path('pizzas', pizzas, name='pizzas'),
    path('order/<int:pk>', order, name='order'),
    path('my_orders/', my_orders, name='myorders'),
]
