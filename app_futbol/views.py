from django.shortcuts import render, get_object_or_404, redirect
from .models import Estadio, Partido
from .forms import EstadioForm, PartidoForm

# Vistas para Partidos
def listar_partidos(request):
    partidos = Partido.objects.all()
    return render(request, 'listar_partidos.html', {'partidos': partidos})

def detalle_partido(request, partido_id):
    partido = get_object_or_404(Partido, id_partido=partido_id)
    return render(request, 'detalle_partido.html', {'partido': partido})

def crear_partido(request):
    if request.method == 'POST':
        form = PartidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_futbol:listar_partidos')
    else:
        form = PartidoForm()
    return render(request, 'formulario_partido.html', {'form': form, 'titulo': 'Crear Partido'})

def editar_partido(request, partido_id):
    partido = get_object_or_404(Partido, id_partido=partido_id)
    if request.method == 'POST':
        form = PartidoForm(request.POST, instance=partido)
        if form.is_valid():
            form.save()
            return redirect('app_futbol:detalle_partido', partido_id=partido.id_partido)
    else:
        form = PartidoForm(instance=partido)
    return render(request, 'formulario_partido.html', {'form': form, 'titulo': 'Editar Partido'})

def borrar_partido(request, partido_id):
    partido = get_object_or_404(Partido, id_partido=partido_id)
    if request.method == 'POST':
        partido.delete()
        return redirect('app_futbol:listar_partidos')
    return render(request, 'confirmar_borrar.html', {'objeto': partido, 'tipo': 'partido'})

# Vistas para Estadios
def listar_estadios(request):
    estadios = Estadio.objects.all()
    return render(request, 'listar_estadios.html', {'estadios': estadios})

def detalle_estadio(request, estadio_id):
    estadio = get_object_or_404(Estadio, id_estadio=estadio_id)
    partidos = estadio.partidos.all()
    return render(request, 'detalle_estadio.html', {'estadio': estadio, 'partidos': partidos})

def crear_estadio(request):
    if request.method == 'POST':
        form = EstadioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_futbol:listar_estadios')
    else:
        form = EstadioForm()
    return render(request, 'formulario_estadio.html', {'form': form, 'titulo': 'Crear Estadio'})

def editar_estadio(request, estadio_id):
    estadio = get_object_or_404(Estadio, id_estadio=estadio_id)
    if request.method == 'POST':
        form = EstadioForm(request.POST, request.FILES, instance=estadio)
        if form.is_valid():
            form.save()
            return redirect('app_futbol:detalle_estadio', estadio_id=estadio.id_estadio)
    else:
        form = EstadioForm(instance=estadio)
    return render(request, 'formulario_estadio.html', {'form': form, 'titulo': 'Editar Estadio'})

def borrar_estadio(request, estadio_id):
    estadio = get_object_or_404(Estadio, id_estadio=estadio_id)
    if request.method == 'POST':
        estadio.delete()
        return redirect('app_futbol:listar_estadios')
    return render(request, 'confirmar_borrar.html', {'objeto': estadio, 'tipo': 'estadio'})