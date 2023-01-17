from django.shortcuts import render

# Create your views here.
#clase 60
# para trabajar con varios modelos, para trabajar con varios modelos usamos FromViews
from django.views.generic.edit import FormView
#clase 61
from .form import NewDepartamentoForm
#clase 62
from Empleado.aplications.empleados.models import Empleados
from .models import Departamento

class NewDepartamentoView(FormView):
    #clase 61 Vista generica Simple Form.Views
    template_name="departamento/61_nuevoDepartamento.html"
    form_class=NewDepartamentoForm
    success_url= '/'

    

    def form_valid(self, form):
        print("estamos validando")
        nombre=form.cleaned_data["nombre"]
        apellidos=form.cleaned_data["apellidos"]
        
        depa=Departamento(
            name=form.cleaned_data["departamento"],
            shor_name=form.cleaned_data["shorname"]
        )
        depa.save()
        
        Empleados.objects.create(
            first_name=nombre,
            last_name=apellidos,
            job="1",
            departamento=depa
        )
        
        return super(NewDepartamentoView, self).form_valid(form)