from django.contrib import admin
from appAsignatura.models import Asignatura

class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre_asignatura', 'code_asignatura', 'carrera', 'is_activa')
    list_select_related = ('carrera',) # Optimiza consultas al mostrar la carrera
    autocomplete_fields = ('carrera',) # Permite buscar carreras por nombre en el admin
    search_fields = ('nombre_asignatura', 'carrera__nombre_carrera')
admin.site.register(Asignatura, AsignaturaAdmin)
# Register your models here.
