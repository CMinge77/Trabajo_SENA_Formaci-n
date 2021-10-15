
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from personas.models import Persona

@login_required
def bienvenido(request):
    no_personas = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id', 'nombre')
    #mensaje = {'mensaje1':'este es el otro mensaje'}
    return render(request, 'bienvenido.html', {'no_personas': no_personas, 'personas': personas})



def conection_web(request):
    mensajes = {'mensaje': 'valor mensaje'}
    return render(request, '(nombre:?)html', mensajes)