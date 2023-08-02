from django.http import HttpResponse
def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to Project</h1></center>'
    )