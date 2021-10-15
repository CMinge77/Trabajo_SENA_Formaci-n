from django.shortcuts import render
from blog.models import Post, Categoria
# Create your views here.
# from mauro.app.models import Servicio
from servicios.models import Servicio

def Blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts': posts})

def categoria(request,  categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render(request, 'blog/categoria.html', {'categoria': categoria, 'posts': posts})