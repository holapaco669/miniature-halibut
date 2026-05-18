from django.db import models
from cloudinary.models import CloudinaryField

class Pelicula(models.Model):
    titulo      = models.CharField(max_length=200)
    anio        = models.IntegerField()
    genero      = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion    = models.CharField(max_length=50)
    imagen      = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.titulo