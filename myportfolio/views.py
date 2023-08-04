from django.shortcuts import render, redirect
from .models import Proyecto, Contacto
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
    if request.method == 'POST':
        try:
            nombre = request.POST['nombre']
            apellidos = request.POST['apellidos']
            email = request.POST['email']
            mensaje = request.POST['mensaje']
            campos = nombre, apellidos, email, mensaje
            for i in campos:
                if i == '':
                    raise Exception
                else:
                    contacto = Contacto.objects.create(nombre=nombre, apellidos=apellidos, email=email, mensaje=mensaje)
                    contacto.save()
                    mensaje_retorno = 'Formulario enviado con exito!'
                    return render(request, 'pages/contact.html', {'mensaje':mensaje_retorno})
            
        except Exception:
            error = 'Hubo un error al enviar al formulario!'
            return render(request, 'pages/contact.html', {'error':error})

    else:
        return render(request, 'pages/contact.html')
    

def comentario(request):
    
    return render(request, 'pages/contact.html')