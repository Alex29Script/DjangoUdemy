from django.shortcuts import render
# 249 
from rest_framework.generics import(
    ListAPIView
)
#250
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
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
    #permission_classes=[IsAuthenticated, IsAdminUser]
    #
    # 253 authentication_classes es el metodo pero quien hace el requerimiento para bloquear la vista
    # es el permission_classes
    #  

    def get_queryset(self):

        # recuperando un usuario
        #enlace con un usuario a travez de manager.py
        
        usuario=self.request.user #usuario de session
        return Product.objects.producto_por_user(usuario)

#254 Paretros por URL
# filtros para productos de hombre o mujer
# modificacion el archivos manage, urls, serializador
class ListaProductosGeneroApiView(ListAPIView):
    serializer_class=ProductSerializer
    #authentication_classes=(TokenAuthentication,)
    #permission_classes=[IsAuthenticated]


    def get_queryset(self):
        genero=self.kwargs['genero'] #genero recuperado de url
        return Product.objects.producto_por_genero(genero)

# 255 Obtner filtros por Parametros
class FiltrarProductosParametrosAPIView(ListAPIView):
    serializer_class=ProductSerializer

    def get_queryset(self):
        varon=self.request.query_params.get('man',None)
        mujer=self.request.query_params.get('woman',None)
        nombre=self.request.query_params.get('name',None)
        return Product.objects.filtrar_productos_parametros(
            man=varon,
            woman=mujer,
            name=nombre
        )


