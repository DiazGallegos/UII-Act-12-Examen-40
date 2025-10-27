from django import forms
from .models import Estadio, Partido

class EstadioForm(forms.ModelForm):
    class Meta:
        model = Estadio
        fields = ['nombre', 'ciudad', 'capacidad', 'fecha_inaguracion', 'direccion', 'cesped_natural', 'imagen_estadio']
        widgets = {
            'fecha_inaguracion': forms.DateInput(attrs={'type': 'date'}),
            'direccion': forms.Textarea(attrs={'rows': 3}),
        }

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ['equipo_local', 'equipo_visitante', 'fecha', 'estadio', 'goles_locales', 'goles_visitantes']
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }