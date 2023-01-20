from django.shortcuts import render
#clase 218
from django.views.generic import (ListView) 



from .models import Person


# clase 219 Django Rest Framework
from rest_framework.generics import (ListAPIView,
#clase 223 CreateApiviews
CreateAPIView,
#Clase 224 RetrieveAPIviews Obetenr un registro
RetrieveAPIView,
# clase 224 Eliminar un registro
DestroyAPIView,
# clase 225 Actualizar un registro Api
UpdateAPIView,
# recuperando datos y actualizando
RetrieveUpdateAPIView
)



class ListaPersonasListView(ListView):
    model = Person
    template_name = "persona/listar.html"
    context_object_name='personas'

    def get_queryset(self):
        
        return Person.objects.all()

#clase 219 Django Rest Framework
# https://www.django-rest-framework.org/
from .serializer import PersonSerializer
# clase 226 serializador desconectado
from .serializer import PersonaSerializer

class PersonListApiView(ListAPIView):
    serializer_class=PersonSerializer
    def get_queryset(self):
        #SERIALIZAR es tranformar datos en json y viceersa
        return Person.objects.all()

#clase 223 Createviews: guardar un regiistro

class PersonCreateview(CreateAPIView):
    serializer_class=PersonSerializer

# clase 224 RetrieveAPIView: Detallar un registro u optenerlo

class PersonDetailsAPIviews(RetrieveAPIView):
    serializer_class=PersonSerializer
    # necesita un query set
    queryset=Person.objects.all()

# clase 224 eliminar un registro
class PersonEliminarAPIviews(DestroyAPIView):
    serializer_class=PersonSerializer
    queryset= Person.objects.all()

# clase 225 actualizar un registro UpdateAPIviews
class PersonActualizaApiviews(UpdateAPIView):
    serializer_class=PersonSerializer
    queryset=Person.objects.all()

class PersonActualizaRetriveApiviews(RetrieveUpdateAPIView):
    serializer_class=PersonSerializer
    queryset=Person.objects.all()

# Serializador desconectado
class PersonaSerListviews(ListAPIView):
    serializer_class=PersonaSerializer
    def get_queryset(self):
        return Person.objects.all()