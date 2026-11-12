from django import forms
from .models import Categoria, Herramienta
import re


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class HerramientaForm(forms.ModelForm):
    class Meta:
        model = Herramienta
        fields = ['codigo', 'nombre', 'categoria', 'estado', 'disponible', 'fecha_ingreso']

    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']

        if not re.fullmatch(r'HER-\d{3}', codigo):
            raise forms.ValidationError('El código debe tener el formato HER-000')

        return codigo
