from django.contrib import admin
from .models import Empleados, Habilidades
# Register your models here.

admin.site.register(Habilidades)

#creando decorador para ver de otra formade mostrar el modelo

class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        "first_name","last_name","departamento","job","full_name",

    )
    #filtro por introduccion de texto
    search_fields=("first_name",)
    #filtros automaticos auto-asistidos
    list_filter=("job","habilidades","departamento")

    # agregando filtro a las habilidades y buscador clase 32
    filter_horizontal= ("habilidades",)

    #creando funciones a los campos nuveos que no se encuentran en el modelo clase 33
    def full_name(self, obj):
        
        return(obj.first_name +" "+obj.last_name)


admin.site.register(Empleados,EmpleadoAdmin)