from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Prueba

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




