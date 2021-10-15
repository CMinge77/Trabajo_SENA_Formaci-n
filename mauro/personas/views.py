# from django.contrib import messages

# from django.forms import modelform_factory
from pyexpat.errors import messages

from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from personas.forms import PersonaForm
from personas.models import Persona

# se crea funcion para detallar personas en django detalle persona.






def detallepersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    #persona = Persona.objects.get(pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})

#VAMOS A DEFINIR UN NUEVO METHODO

# PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('Inicio')
    else:
        formaPersona = PersonaForm()
    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})

def editPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona)

        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('Inicio')
    else:

        formPersona = PersonaForm(instance=persona)
    return render(request, 'personas/editar.html', {'formaPersona': formPersona})

def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('Inicio')
