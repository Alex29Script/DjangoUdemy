from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView
    
)
from .models import Sale

from .serializers import VentaReporteSerializers
# Create your views here.


# 256 Json dentro de Json
# realizar un reporte de ventas y los detalles de cada venta
class ReporteVentasList(ListAPIView):
    serializer_class=VentaReporteSerializers

    def get_queryset(self):
        
        return Sale.objects.all()
