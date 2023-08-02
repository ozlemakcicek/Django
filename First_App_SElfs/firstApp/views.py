from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hellooo...")

def students(request):
    return HttpResponse("merhaba")

def teachers(request):
    return HttpResponse("guten Tag")    
