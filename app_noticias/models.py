from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Titulo de la noticia")
    fecha = models.DateField(verbose_name="Fecha de ocurrencia")
    lugar = models.CharField(max_length=200, verbose_name="Lugar")
    descripcion = models.TextField(verbose_name="Descripcion")
    imagen = models.ImageField(upload_to="app_noticias/", verbose_name="Imagen")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")

class Meta:
    ordering = ['-fecha']
    verbose_name = "Noticia"
    verbose_name_plural = "Noticias"

def __str__(self):
    return self.titulo