from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dswel(request):
    return HttpResponse("DS sayfasina hosgeldiniz")