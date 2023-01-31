from django.utils import timezone
#
from django.shortcuts import render
#
from rest_framework.generics import (
    ListAPIView, CreateAPIView
    
)
from rest_framework.response import Response

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Sale,SaleDetail

from applications.producto.models import Product

from .serializers import (
    VentaReporteSerializers,
    ProcesoVentaSerializer
    )
# Create your views here.


# 256 Json dentro de Json
# realizar un reporte de ventas y los detalles de cada venta
class ReporteVentasList(ListAPIView):
    serializer_class=VentaReporteSerializers

    def get_queryset(self):
        
        return Sale.objects.all()

# 258 Serializador sobre serializadores
# Registrar una venta

class RegistroVentaApiViews(CreateAPIView):
    authentication_classes=(TokenAuthentication,)
    permission_classes=[IsAuthenticated]

    serializer_class=ProcesoVentaSerializer

    #sobreescribiendo la funcion create dado que los serializadores no estan conectados
    def create(self, request, *args, **kwargs):
        des_serializer=ProcesoVentaSerializer(data=request.data) #obteniendo los datos
        # importante validar los datos
        des_serializer.is_valid(raise_exception=True)
        # confirmar datos (opcional)
        respuesta={
            "tipo_recibo":des_serializer.validated_data["type_invoce"],
            "tipo_venta":des_serializer.validated_data["type_payment"]
            
        }
        print("***********Respuesta************")
        print(respuesta)
        #259
        venta=Sale.objects.create(
            date_sale=timezone.now(),
            amount=0,
            count=0,
            type_invoce= des_serializer.validated_data["type_invoce"],
            type_payment=des_serializer.validated_data["type_payment"],
            adreese_send=des_serializer.validated_data["adreese_send"],
            user=self.request.user,
        )
        #259 recuperando productos
        productos=des_serializer.validated_data["productos"]
        print(productos)

        #260 Bull create
        #iterar para bull create
        ventas_detalle=[]
        amount=0
        count=0
        

        for producto in productos:
            prod=Product.objects.get(id=producto['pk'])
            venta_detalle=SaleDetail(
                sale=venta,
                product=prod,
                count=producto['count'],
                price_purchase=prod.price_purchase,
                price_sale=prod.price_sale,
                )
            #260
            amount=amount+prod.price_sale*producto["count"]
            count=count+producto["count"]
            ventas_detalle.append(venta_detalle)
        
        venta.amount=amount
        venta.count=count
        venta.save()

        SaleDetail.objects.bulk_create(ventas_detalle)

        return Response({'code':'ok'})
        
