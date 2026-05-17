from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    genero = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    fecha_estreno = models.DateField()
    imagen = models.URLField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
