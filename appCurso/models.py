from django.db import models
from appAsignatura.models import Asignatura
# Create your models here.
class Curso(models.Model):
    asignatura = models.ForeignKey(Asignatura,
                on_delete=models.CASCADE,
                related_name='cursos',
                null=True,
                blank=True
                )
    nombre_curso = models.CharField(max_length=100)
    code_curso = models.CharField(max_length=20, unique=True)
    grupo_curso = models.CharField(max_length=10, default='Grupo-A')
    tipo_periodo = models.CharField(max_length=20, 
            choices=[('Semestral', 'Semestral'), ('Anual', 'Anual'),('VERANO', 'Verano')]
        )
    is_activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_curso
