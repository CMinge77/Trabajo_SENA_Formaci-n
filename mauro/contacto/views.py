from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.



@login_required
def Contacto(request):
    formulario_contacto = FormularioContacto()
    if request.method =='POST':
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')
 
            email=EmailMessage("mensaje desde la pagina", 
            "El usuario con nombre {} con la direccion {} escribe lo siguiente:\n\n {}".format(nombre, email, contenido), 
            "", ["mauro200877@gmail.com"],reply_to=[email])

            try:
                email.send()
                return redirect('/contacto/?enviado')
            except:
                return redirect('/contacto/?noenviado')

    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})