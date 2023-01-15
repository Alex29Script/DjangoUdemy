from django.shortcuts import render
#documentacion para vista genericas https://ccbv.co.uk/
# Create your views here.

#36.a importamos los generico de Django
from django.views.generic import (
    ListView,
    #clase 43
    DetailView
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
# Clase 42 Relacion Many to many en Listview
class ListHabilidadesEmpleado(ListView):
    template_name="empleados/habilidadesEmpleado.html"
    context_object_name="habilidadesEmpleado"

    def  get_queryset(self):
        #https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_many/
        empleado=Empleados.objects.get(id=4)
        
        return empleado.habilidades.all() 


#clase 43
#Tipo de vista generica Detailviews: su funcion es ver los detalles de un registro del modelo

class EmpleadoDetailView(DetailView):
    model = Empleados
    template_name = "empleados/detalleEmpleado.html"

    # rescribiendo un metodo del DetailViews
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context["titulo"]=" <> Empleado del Mes <>"
        return context
     
