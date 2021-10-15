from django.db import models



class Servicio(models.Model):
      nombre=models.CharField(max_length=250)
      titulo=models.CharField(max_length=50)
      contenido=models.CharField(max_length=50)
      imagen=models.ImageField(upload_to="blog", null=True, blank=True)
      created = models.DateTimeField(auto_now_add=True)
      update = models.DateTimeField(auto_now_add=True)

      class Meta:
            verbose_name ='servicio'
            verbose_name_plural ='servicios'

      def __str__(self):
                  return self.titulo


# class categoria(models.Model):
#     nombre=models.CharField(max_length=50)
#     created=models.DateTimeField(auto_now_add=True)
#     update = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name ='categoria'
#         verbose_plural ='categorias'

#     def __str__(self):
#             return self.nombre


# class post(model.Model):
#     titulo = models.CharField(max_length=50)
#     contenido = models.CharField(max_length=50)
#     imagen = models.ImageField(upload_to="blog", null=True, blank=True)
#     autor = models.ForeignKey(User, on_delete=models.CASCADE) 
#     categorias = ManyToManyField(categoria)
#     created = models.DateTimeField(auto_now_add=True)
#     update = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name ='post'
#         verbose_plural =''

#     def __str__(self):
#             return self.nombre
