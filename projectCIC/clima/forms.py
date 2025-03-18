from django import forms
from .models import Datos

class datosForm(forms.ModelForm):
    class Meta:
        model = Datos
        fields = ['ciudad', 'temperatura', 'humedad']