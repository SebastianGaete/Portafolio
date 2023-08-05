from django.shortcuts import render, redirect
from .models import Proyecto, Contacto, Comentario
# Create your views here.

def home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos':proyectos})


def about(request):
    comentarios = Comentario.objects.all()
    ninguno = 'Se la primera persona en comentar!'
    if comentarios:
        return render(request, 'pages/about.html', {'comentarios':comentarios})
    else:
        return render(request, 'pages/about.html', {'comentarios':comentarios, 'ninguno':ninguno})


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
    

def comentarios(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contenido = request.POST['contenido']
        comentario = Comentario.objects.create(usuario=usuario, contenido=contenido)
        comentario.save()
        print(comentario)
        return redirect('about')
    else:
        return render(request, 'pages/about.html')