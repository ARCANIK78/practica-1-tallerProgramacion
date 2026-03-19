from django.contrib import admin
from appCurso.models import Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre_curso', 'code_curso', 'asignatura', 'grupo_curso', 'tipo_periodo')
    search_fields = ('nombre_curso',)
    list_select_related = ('asignatura',) # Optimiza consultas al mostrar asignatura
    autocomplete_fields = ('asignatura',) # Permite buscar asignaturas por nombre en el admin
admin.site.register(Curso, CursoAdmin)
# Register your models here.
