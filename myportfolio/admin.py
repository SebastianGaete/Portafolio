from django.contrib import admin
from .models import Proyecto
# Register your models here.

@admin.register(Proyecto)
class AdminProyecto(admin.ModelAdmin):
    pass

