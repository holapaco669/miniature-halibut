from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .models import Post #importar el modelo
from datetime import datetime

def publicaciones(request):
   posts = Post.objects.all().order_by('-fecha')
   return render(request, 'blog/publicaciones.html', {'posts': posts})

def crear_post(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        contenido = request.POST.get("contenido", "")

        if not titulo:
            return render(request, "blog/crear.html", {
                "error": "El título no puede estar vacío"
            })

        Post.objects.create(
            titulo=titulo,
            contenido=contenido
        )
        return redirect("publicaciones")

    return render(request, "blog/crear.html")

def api_posts(request):
    posts = Post.objects.all().values('id', 'titulo', 'contenido', 'fecha', 'autor')
    return JsonResponse(list(posts), safe=False)

from django.shortcuts import get_object_or_404

def api_post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    data = {
        'id': post.id,
        'titulo': post.titulo,
        'contenido': post.contenido,
        'fecha': post.fecha,
        'autor': post.autor,
    }
    return JsonResponse(data)

def api_json(request):
    return render(request, 'blog/api.html')

