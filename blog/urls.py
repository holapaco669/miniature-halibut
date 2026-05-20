from django.urls import path
from . import views
 
urlpatterns = [
    # 🎬 INTERFAZ
    path('', views.peliculas, name='peliculas'),
    path('crear/', views.crear_pelicula, name='crear_pelicula'),
    path('pelicula/<int:id>/', views.detalle_pelicula, name='detalle_pelicula'),  # ← NUEVO
 
    # 🌐 API
    path('api/peliculas/', views.api_peliculas, name='api_peliculas'),
    path('api/peliculas/<int:id>/', views.api_pelicula_detail, name='api_pelicula_detail'),
    path('api/json/', views.api_json, name='json_api'),
]
 
path('borrar-todo/', views.borrar_todo, name='borrar_todo'),