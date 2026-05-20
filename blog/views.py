from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Pelicula
 
 




def peliculas(request):
    lista = Pelicula.objects.all().order_by('-id')
    return render(request, 'blog/peliculas.html', {'peliculas': lista})
 
 

def detalle_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    return render(request, 'blog/detalle.html', {'pelicula': pelicula})
 


def crear_pelicula(request):
    if request.method == "POST":
        titulo      = request.POST.get("titulo", "").strip()
        descripcion = request.POST.get("descripcion", "")
        genero      = request.POST.get("genero", "")
        anio        = request.POST.get("anio", "")
        duracion    = request.POST.get("duracion", "")
        imagen      = request.FILES.get("imagen")
 
        if not titulo:
            return render(request, "blog/crear.html", {"error": "El título no puede estar vacío"})
        if not imagen:
            return render(request, "blog/crear.html", {"error": "Debes subir una imagen"})
 
        Pelicula.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            genero=genero,
            anio=anio,
            duracion=duracion,
            imagen=imagen
        )
        return redirect("peliculas")
 
    return render(request, "blog/crear.html")
 
 
# 📌 API: TODAS LAS PELÍCULAS
def api_peliculas(request):
    data = Pelicula.objects.all().values('id', 'titulo', 'descripcion', 'genero', 'anio', 'duracion')
    return JsonResponse(list(data), safe=False)
 
 
# 📌 API: DETALLE
def api_pelicula_detail(request, id):
    pelicula = get_object_or_404(Pelicula, id=id)
    data = {
        'id':          pelicula.id,
        'titulo':      pelicula.titulo,
        'descripcion': pelicula.descripcion,
        'genero':      pelicula.genero,
        'anio':        pelicula.anio,
        'duracion':    pelicula.duracion,
        'imagen':      pelicula.imagen.url if pelicula.imagen else None,
    }
    return JsonResponse(data)
 
 
# 📌 INTERFAZ API
def api_json(request):
    return render(request, 'blog/api.html')


#from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def borrar_todo(request):
    Pelicula.objects.all().delete()
    return redirect('peliculas')