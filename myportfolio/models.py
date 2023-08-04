from django.db import models

# Create your models here.

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='proyectos')
    link = models.URLField(blank=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    

class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    email = models.EmailField()
    mensaje =models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')

    def __str__(self):
        return self.nombre + " " + self.apellidos
