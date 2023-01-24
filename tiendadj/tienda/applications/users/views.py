from django.shortcuts import render

# Create your views here.

#clase 236 codigo para auth con google
from django.views.generic import TemplateView

class loginTemplateView(TemplateView):
    template_name='users/236login.html'