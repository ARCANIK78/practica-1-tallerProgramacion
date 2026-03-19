from django.db import models
from appCarrera.models import Carrera

class Estudiante(models.Model):
    nombre_estudiante = models.CharField(max_length=100)
    ru_estudiante = models.CharField(max_length=20, unique=True)
    anio_ingreso = models.PositiveIntegerField()
    carrera = models.ForeignKey(Carrera,
                on_delete=models.CASCADE, 
                related_name='estudiantes',
                null=True, 
                blank=True)
    
    def __str__(self):
        return self.nombre_estudiante
# Create your models here.
