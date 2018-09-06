from django import forms

from .models import Proyecto, Desarrollo


class ProyectoForm(forms.ModelForm):

    class Meta:
        model = Proyecto

        fields = [
            'nombre',
            'modulo',
            'descripcion',
            'notas',
        ]
        labels = {
            'nombre': 'Nombre',
            'modulo': 'Módulo',
            'descripcion': 'Descripción',
            'notas': 'Notas',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'modulo': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'notas': forms.Textarea(attrs={'class':'form-control'}),
        }


class DesarrolloForm(forms.ModelForm):

    class Meta:
        model = Desarrollo

        fields = [
            'proyecto',
            'version',
            'consultas',
            'informacion',
            'estatus',
        ]
        labels = {
            'proyecto': 'Proyecto del Desarrollo',
            'version': 'Versión',
            'consultas': 'Consultas Relevantes',
            'informacion': 'Información',
            'estatus': 'Status',
        }
        widgets = {
            'proyecto': forms.Select(attrs={'class':'form-control'}),
            'version': forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'consultas': forms.Textarea(attrs={'class':'form-control'}),
            'informacion': forms.Textarea(attrs={'class':'form-control'}),
            'estatus': forms.Select(attrs={'class':'form-control'}),
        }