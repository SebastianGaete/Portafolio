from django.contrib import admin
from .models import Proyecto, Contacto
# Register your models here.

@admin.register(Proyecto)
class AdminProyecto(admin.ModelAdmin):
    pass


@admin.register(Contacto)
class AdminContacto(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email', 'fecha_envio')
    readonly_fields = ('fecha_envio',)