from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    anio = models.IntegerField()
    genero = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.CharField(max_length=50)

    imagen = models.ImageField(upload_to='peliculas/', blank=True, null=True)

    def __str__(self):
        return self.titulo