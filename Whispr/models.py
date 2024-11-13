from django.db import models

# Create your models here.
class Reunion(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    duracion = models.DurationField()
    