from django.shortcuts import render
#clase 218
from django.views.generic import ListView
from .models import Person
# clase 219 Django Rest Framework
from rest_framework.generics import ListAPIView



class ListaPersonasListView(ListView):
    model = Person
    template_name = "persona/listar.html"
    context_object_name='personas'

    def get_queryset(self):
        
        return Person.objects.all()

#clase 219 Django Rest Framework
# https://www.django-rest-framework.org/
from .serializer import PersonSerializer


class PersonListApiView(ListAPIView):
    serializer_class=PersonSerializer
    def get_queryset(self):
        #SERIALIZAR es tranformar datos en json y viceersa
        return Person.objects.all()





