from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Perfil (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='perfil', null=True, blank=True)

    def __str__(self):
        return f'perfil de: {self.user.username}'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'



# class Registro(models.Model):
#     email = models.EmailField()
#     password1 = models.CharField(widget=models.PasswordInput)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
#     password2 = models.CharField(max_length=50, widget=models.PasswordInput)

