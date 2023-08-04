from django.shortcuts import render, redirect
from .models import Proyecto
# Create your views here.

def home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos':proyectos})