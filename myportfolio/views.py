from django.shortcuts import render, redirect
from .models import Proyecto
# Create your views here.

def home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos':proyectos})

def about(request):
    return render(request, 'pages/about.html')

def detail_project(request, id):
    detalle = Proyecto.objects.get(id=id)
    return render(request, 'pages/detail_project.html', {'detalle':detalle})

def contact(request):
    return render(request, 'pages/contact.html')