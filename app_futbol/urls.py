from django.urls import path
from . import views

app_name = 'app_futbol'

urlpatterns = [
    # Partidos
    path('', views.listar_partidos, name='listar_partidos'),
    path('partidos/<int:partido_id>/', views.detalle_partido, name='detalle_partido'),
    path('partidos/crear/', views.crear_partido, name='crear_partido'),
    path('partidos/editar/<int:partido_id>/', views.editar_partido, name='editar_partido'),
    path('partidos/borrar/<int:partido_id>/', views.borrar_partido, name='borrar_partido'),
    
    # Estadios
    path('estadios/', views.listar_estadios, name='listar_estadios'),
    path('estadios/<int:estadio_id>/', views.detalle_estadio, name='detalle_estadio'),
    path('estadios/crear/', views.crear_estadio, name='crear_estadio'),
    path('estadios/editar/<int:estadio_id>/', views.editar_estadio, name='editar_estadio'),
    path('estadios/borrar/<int:estadio_id>/', views.borrar_estadio, name='borrar_estadio'),
]