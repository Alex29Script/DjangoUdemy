from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class admin_prueba_app(TemplateView):
    template_name='admin_django/admin_prueba.html'