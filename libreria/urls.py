from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('Favoritos', views.Favoritos, name='Favoritos'),
    path('libros',views.mangas, name='mangas'),
    path('libros/Leer',views.leermanga, name='Leer'),
    path('libros/cap1one',views.cap1one, name='Capitulo1One'),
]