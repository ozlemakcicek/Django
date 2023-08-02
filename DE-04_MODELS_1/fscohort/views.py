from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fswelcome(request):
    return HttpResponse("FS sayfasina hosgeldiniz")
