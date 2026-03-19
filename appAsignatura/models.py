from django.db import models
from appCarrera.models import Carrera

# Create your models here.
class Asignatura(models.Model):
    nombre_asignatura = models.CharField(max_length=100)
    code_asignatura = models.CharField(max_length=15, unique=True)
    descripcion_asignatura = models.TextField(blank=True, null=True)
    is_activa = models.BooleanField(default=True)
    carrera = models.ForeignKey(Carrera, 
                on_delete=models.CASCADE, 
                related_name='asignaturas',
                null=True, 
                blank=True)
    
    def __str__(self):
        return self.nombre_asignatura
