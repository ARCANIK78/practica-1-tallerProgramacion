from django.contrib import admin
from appEstudiantes.models import Estudiante

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre_estudiante', 'ru_estudiante', 'anio_ingreso', 'carrera')
    search_fields = ('nombre_estudiante', 'carrera__nombre_carrera')
    list_select_related = ('carrera',) # Optimiza consultas al mostrar la carrera
    autocomplete_fields = ('carrera',) # Permite buscar carreras por nombre en el admin
admin.site.register(Estudiante, EstudianteAdmin)

# Register your models here.
