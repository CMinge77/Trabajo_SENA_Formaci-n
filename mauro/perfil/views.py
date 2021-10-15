# from pyexpat.errors import messages
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
# from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from .forms import UserRegisterForm, PostForm


def new(request):

    return render(request, 'perfil/login.html')
@login_required
def feed(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'perfil/usuarios.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} ha sido creado')
            return redirect('nuevo')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'perfil/register.html', context)

@login_required
def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form =PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Enviado')
            return redirect('usuario')

    else:
        form = PostForm()
    return render(request, 'perfil/post.html', {'form': form})


@login_required
def perfil(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, 'perfil/perfil.html', {'user': user, 'posts': posts})
