from django.db import models

# Create your models here.
from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Reunion(models.Model):
    titulo = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    duracion = models.DurationField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='reuniones', null=True, blank=True)  # Permite valores nulos
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.empresa.nombre if self.empresa else 'Sin Empresa'}"

    
class Transcripcion(models.Model):
    ESTADO_OPCIONES = [
        ('EN_PROCESO', 'En Proceso'),
        ('COMPLETADA', 'Completada'),
    ]
    
    reunion = models.ForeignKey(Reunion, on_delete=models.CASCADE, related_name='transcripciones')
    texto = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADO_OPCIONES, default='EN_PROCESO')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transcripción de {self.reunion.titulo} - Estado: {self.estado}"
    
class Analisis(models.Model):
    transcripcion = models.ForeignKey(Transcripcion, on_delete=models.CASCADE, related_name='analisis')
    resumen = models.TextField()
    puntos_clave = models.TextField()
    sugerencias = models.TextField()
    fecha_analisis = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Análisis de {self.transcripcion.reunion.titulo} - Fecha: {self.fecha_analisis}"

    