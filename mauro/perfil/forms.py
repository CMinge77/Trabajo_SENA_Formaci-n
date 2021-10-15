from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraceña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma contraceña', widget=forms.PasswordInput)

    class Meta:
      model = User
      fields = ['username', 'password1', 'password2']
      help_texts = {k:"" for k in fields }

class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':1, 'placeholder':'¿Como Podemos Ayudarte?: '}), required=True)

    class Meta:
        model = Post
        fields = ['content']