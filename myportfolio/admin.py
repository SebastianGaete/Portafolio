from django.contrib import admin
from .models import Proyecto, Contacto, Comentario, Certificado
# Register your models here.

@admin.register(Proyecto)
class AdminProyecto(admin.ModelAdmin):
    pass


@admin.register(Contacto)
class AdminContacto(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email', 'fecha_envio')
    readonly_fields = ('fecha_envio',)


@admin.register(Certificado)
class AdminCerificado(admin.ModelAdmin):
    list_display = ('nombre_certificado', 'fecha_obtencion')


@admin.register(Comentario)
class AdminComentario(admin.ModelAdmin):
    list_display = ('usuario', 'fecha_comentario',)
