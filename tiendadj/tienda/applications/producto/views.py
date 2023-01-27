from django.shortcuts import render
# 249 
from rest_framework.generics import(
    ListAPIView
)
#250
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
#
# Create your views here.

#modelos
#249
from .models import Product


#Serializadores
#249
from .serializers import ProductSerializer

#Managers
#250

#

#249 Listar Productos en json

class ListaProductosApiView(ListAPIView):
    serializer_class=ProductSerializer
    #250 Autenticacion
    authentication_classes=(TokenAuthentication,)
    permission_classes=[IsAuthenticated]
    #

    def get_queryset(self):

        # recuperando un usuario
        #enlace con un usuario a travez de manager.py
        
        usuario=self.request.user #usuario de session
        return Product.objects.producto_por_user(usuario)

