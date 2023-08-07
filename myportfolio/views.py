from django.shortcuts import render, redirect
from .models import Proyecto, Comentario, Certificado

from .forms import Crear_contacto, Crear_comentario
# Create your views here.

def home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'index.html', {'proyectos':proyectos})


def about(request):
    certificados = Certificado.objects.all().order_by('-id')
    comentarios = Comentario.objects.all().order_by('-fecha_comentario')
    ninguno = 'Se la primera persona en comentar!'
    if comentarios:
        return render(request, 'pages/about.html', {
            'comentarios':comentarios, 
            'certificados':certificados, 
            'formulario_comentario':Crear_comentario
            })
    else:
        return render(request, 'pages/about.html', {
            'comentarios':comentarios, 
            'ninguno':ninguno, 
            'certificados':certificados, 
            'formulario_comentario':Crear_comentario
            })



def contact(request):
    if request.method == 'POST':
        try:
            formulario = Crear_contacto(request.POST)
            contacto = formulario.save(commit=False)
            campos = contacto.nombre, contacto.apellidos, contacto.email, contacto.mensaje
            
            for i in campos:
                if campos[i] == '' :
                    raise Exception
                else:
                    contacto.save()
                    mensaje_retorno = 'Formulario enviado con exito!'
                    return render(request, 'pages/contact.html', {'mensaje':mensaje_retorno, 'formulario_contacto': Crear_contacto})
            
        except Exception:
            error = 'Hubo un error al enviar al formulario!'
            return render(request, 'pages/contact.html', {'error':error, 'formulario_contacto': Crear_contacto})
    else:
        return render(request, 'pages/contact.html', {'formulario_contacto': Crear_contacto})
    

def comentarios(request):
    if request.method == 'POST':
        formulario = Crear_comentario(request.POST)
        formulario.save()
        return redirect('about')
    else:
        return render(request, 'pages/about.html')
    

def certificados(request):
    return render(request, 'pages/about.html')