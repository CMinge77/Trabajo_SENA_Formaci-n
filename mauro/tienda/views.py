from django.shortcuts import render
# from django.countrib
from .models import Producto
# Create your views here.

# @method_decorator(login_required)
def tienda(request):

    productos=Producto.objects.all()
  
    return render(request, "tienda/tienda.html", {"productos": productos})