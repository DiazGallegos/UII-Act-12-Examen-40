from django.contrib import admin
from .models import Estadio, Partido

@admin.register(Estadio)
class EstadioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ciudad', 'capacidad', 'fecha_inaguracion']
    list_filter = ['ciudad', 'cesped_natural']
    search_fields = ['nombre', 'ciudad']

@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ['equipo_local', 'equipo_visitante', 'fecha', 'estadio', 'goles_locales', 'goles_visitantes']
    list_filter = ['estadio', 'fecha']
    search_fields = ['equipo_local', 'equipo_visitante']