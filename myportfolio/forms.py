from django import forms

from .models import Contacto, Comentario

class Crear_contacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'apellidos', 'email', 'mensaje']

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control campo_input opacity-50 shadow-none border-0', 'placeholder':'Nombre*', 'label':''}),
            'apellidos':forms.TextInput(attrs={'class':'form-control campo_input opacity-50 shadow-none border-0', 'placeholder':'Apellidos*', 'label':''}),
            'email':forms.EmailInput(attrs={'class':'form-control campo_input opacity-50 shadow-none border-0', 'placeholder':'Email*', 'label':''}),
            'mensaje':forms.Textarea(attrs={'class':'form-control campo_input opacity-50 shadow-none border-0', 'rows':4, 'placeholder':'Deja tu mensaje*', 'label':''}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''
            field.required = None


class Crear_comentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['usuario', 'contenido']

        widgets = {
            'usuario':forms.TextInput(attrs={'class':'form-control shadow-none border-0 mb-2', 'placeholder':'Nombre*'}),
            'contenido':forms.Textarea(attrs={'class':'form-control shadow-none border-0', 'rows':4, 'placeholder':'Comentario*'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''