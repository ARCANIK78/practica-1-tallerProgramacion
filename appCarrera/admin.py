from django.contrib import admin
from appCarrera.models import Carrera 

class CarreraAdmin(admin.ModelAdmin):
    search_fields = ('nombre_carrera',)

admin.site.register(Carrera, CarreraAdmin)
