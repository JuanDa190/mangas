from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'paginas/inicio.html')

def Favoritos(request):
    return render(request, 'paginas/Favoritos.html')

def mangas(request):
    return render(request, 'libros/index.html')

def leermanga(request):
    return render(request, 'libros/Leer.html')

def cap1one(request):
    return render(request, 'libros/cap1one.html')
