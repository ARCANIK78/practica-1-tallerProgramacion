from django.contrib import admin
from appProgramacion.models import Programacion
class ProgramacionAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso', 'fecha_programacion')
    list_select_related = ('estudiante', 'curso') # Optimiza consultas al mostrar estudiante y curso
    autocomplete_fields = ('estudiante', 'curso') # Permite buscar estudiantes y cursos por
admin.site.register(Programacion, ProgramacionAdmin)
# Register your models here.
