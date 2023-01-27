from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Prueba
#Clase 57 Formularios
from .form import PruebaForm

# Create your views here.

class indexView(TemplateView):
    template_name='home/home.html'

class PruebaListView(ListView):
    template_name="home/lista.html"
    queryset=["A","B","C"]
    context_object_name="lista_prueba"

class ListarPruebas(ListView):
    template_name="home/lista_prueba.html"
    model=Prueba
    context_object_name="pruebas"

#clase 56 Formularios en Django
class PruebaCreateView(CreateView):
    template_name='home/add.html'
    model=Prueba
    form_class=PruebaForm
    success_url='/'


class GrillasTemplateView(TemplateView):
    template_name = "home/70Grillas.html"
