from django.shortcuts import render
#documentacion para vista genericas https://ccbv.co.uk/
#clase 48 importando libreria necesaria
from django.urls import reverse_lazy

# Create your views here.

#36.a importamos los generico de Django
from django.views.generic import (
    ListView,
    #clase 43
    DetailView,
    #clase 45
    CreateView,
    #clase 48
    TemplateView,
    #clase 51
    UpdateView,
    #clase 54
    DeleteView
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


# clase 48 Realacion CreateView and TemplateViews

class SuccessView(TemplateView):
    template_name = "empleados/48success.html"



#clase 45-46 CreateViews
#vista para crear nuevos registros

class EmpleadoCreateView(CreateView):
    model = Empleados
    template_name = "empleados/45CrearEmpleado.html"
    # requiere un parametro mas el fields, este es una forma donde elegimos los campos
    #fields=['first_name',"last_name","job"]
    #Clase 46 registrando todos lo campo de empleado de forma mas facil
    #fields=('__all__')
    #clase 49 al agregar fullname como campo deseo escoger cuales se van a ver en la vista
    fields=[
        "first_name",
        "last_name",
        "job",
        "departamento",
        'habilidades',
        
    ]
    #clase 47 guardado y redireccionado
    #success_url='CrearEmpleado' no es buena practica
    #clase 48
    success_url = reverse_lazy('empleados_app:correcto')
    #clase 49
    
    def form_valid(self, form): # interviene el datos guardados PERO guardando
        empleado=form.save(commit=False)#todos los datos del formulario lo hemos captturado en la variable empleado
        empleado.full_name=empleado.first_name+' '+empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_invalid(form)
    
#clase 51 Updateviews: actualizar un registro
class EmpleadosUpdateView(UpdateView):
    model = Empleados
    template_name = "empleados/51updateEmpleado.html"
    fields=[
        "first_name",
        "last_name",
        "job",
        "departamento",
        'habilidades',
    ]
    success_url=reverse_lazy("empleados_app:correcto")
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        
        return super(EmpleadosUpdateView, self).form_valid(form)

#clase 54 Eliminar Deleteviews

class EliminarEmpleadoDeleteView(DeleteView):
    model = Empleados
    template_name = "empleados/54eliminarEmpleados.html"
    success_url=reverse_lazy("empleados_app:correcto")
    #se debe hacer una pregunta de confirmacion