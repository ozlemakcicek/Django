from django.shortcuts import render,HttpResponse

from .models import Category
from .serializers import CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Post
from .serializers import PostSerializer

# Create your views here.
def home(request):
    return HttpResponse('<center><h1 style="background-color:powderblue;">Welcome to Project</h1></center>')

@api_view(['GET', 'POST'])
def category(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Category name {serializer.validated_data.get('name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def post(request):
    if request.method == 'GET':
        categories = Post.objects.all()
        serializer = PostSerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Category name {serializer.validated_data.get('name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)