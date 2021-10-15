from django.shortcuts import render


# Create your views here.

def Home(request):
    return render(request, "app/Home.html")


def index(request):
    return render(request, "app/index.html")


def Portafolio(request):
    return render(request, "app/portafolio.html")







