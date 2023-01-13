from django.shortcuts import render
#documentacion para vista genericas https://ccbv.co.uk/
# Create your views here.

#36.a importamos los generico de Django
from django.views.generic import (
    ListView,    
)


###clase 36 listViews
## supongamos que nos piden estos requerimientos

# 1. Lista de los empleados
#36.b
from .models import Empleados
#36.c
class ListAllEmpleados(ListView):
    template_name="empleados/list_all_empleados.html"
    model=Empleados #hasta aca funcionaria perfectamente
    # aca se puede cargar el obketo accediento a object_list
    #clase 41 Paginacion de registros
    paginate_by=3

# 2 Lista de los empleados que pertenecen a un area de la empresa
#clase 37 Filtros en Listas
class ListByAreaEmpleado(ListView):
    template_name="empleados/list_all_empleados_by_area.html"
    #queryset=Empleados.objects.filter( # buscar app departamentos
    #    departamento__shor_name='Produccion'
    #)
    #clase 38 otra forma de hacer filtros
    def get_queryset(self):
        area=self.kwargs["shorname"] # recupera los argumentos que se mandan por la urls
        lista=Empleados.objects.filter( # buscar app departamentos
        departamento__shor_name=area
        )
        return lista     



# 3 Lista de los empleados por trabajo
#

# 4 Lista de los empleados por palabra clave
#clase 40

class ListEmpleadosByKword(ListView):
    template_name="empleados/ByKwords.html"
    context_object_name="empleados"

    def get_queryset(self):
        print("*************************")
        palabra_clave=self.request.GET.get("kword","")
        lista=Empleados.objects.filter( # buscar app departamentos
        first_name=palabra_clave
        )
        print("lista persona:" ,lista)
        return lista




# 5 Lista habilidades de un empleado