from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
# from mauro.app.models import Servicio
from servicios.models import Servicio, Categoria_servicios


def Servicios(request):
    servicios = Servicio.objects.all()

    return render(request, "servicios/servicios.html", {'servicios':servicios})

@login_required
def CategoriaServicios(request,  categoria_servicios_id):
    categoria_servicios = Categoria_servicios.objects.get(id=categoria_servicios_id)
    servicios = Servicio.objects.filter(categorias=categoria_servicios)

    return render(request, 'servicios/categoria_servicios.html', {'categoria_servicios': categoria_servicios, 'servicios': servicios})