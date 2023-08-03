from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import(
    Category,CategorySerializer,
    Post,PostSerializer
)

# Create your views here.
class CategoryView(ModelViewSet):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer


class PostView(ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    
