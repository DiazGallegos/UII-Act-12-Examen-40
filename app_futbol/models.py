from django.db import models

class Estadio(models.Model):
    TIPO_CESPED = [
        ('natural', 'Natural'),
        ('artificial', 'Artificial'),
        ('mixto', 'Mixto'),
    ]
    
    id_estadio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    fecha_inaguracion = models.DateField()
    direccion = models.TextField()
    cesped_natural = models.CharField(max_length=10, choices=TIPO_CESPED, default='natural')
    imagen_estadio = models.ImageField(upload_to='img_estadios/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.ciudad}"

    class Meta:
        verbose_name = "Estadio"
        verbose_name_plural = "Estadios"

class Partido(models.Model):
    id_partido = models.AutoField(primary_key=True)
    equipo_local = models.CharField(max_length=100)
    equipo_visitante = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE, related_name='partidos')
    goles_locales = models.IntegerField(default=0)
    goles_visitantes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante} - {self.fecha.strftime('%d/%m/%Y')}"

    def resultado(self):
        return f"{self.goles_locales} - {self.goles_visitantes}"

    class Meta:
        verbose_name = "Partido"
        verbose_name_plural = "Partidos"
        ordering = ['-fecha']