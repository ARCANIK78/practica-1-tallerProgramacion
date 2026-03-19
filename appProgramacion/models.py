from django.db import models
from appEstudiantes.models import Estudiante
from appCurso.models import Curso
from datetime import date

class Programacion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='programaciones')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='programaciones')
    fecha_programacion = models.DateField(default=date.today)

    class Meta:
        unique_together = ('estudiante', 'curso')  # Evita que un estudiante se programe en el mismo curso más de una vez

    def __str__(self):
        return f"{self.estudiante} - {self.curso}"
# Create your models here.
