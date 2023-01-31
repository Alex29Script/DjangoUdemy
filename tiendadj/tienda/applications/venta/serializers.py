from rest_framework import serializers

from .models import ( Sale,SaleDetail)

#256 Modelo de Reporte
class VentaReporteSerializers(serializers.ModelSerializer):
    
    #257 agregando la lista de productos a las vetnas
    productos=serializers.SerializerMethodField()
    #
    
    
    class Meta:
        model=Sale
        fields=(
            'id',
            'date_sale',
            'amount',
            'count',
            'type_invoce',
            'cancelado',
            'type_payment',
            'state',
            'adreese_send',
            'anulate',
            'user',
            'productos'
        )
    #257
    def get_productos(self,obj):
        query = SaleDetail.objects.productos_por_venta(obj.id)
        productos_serializado=DetalleVentaProductoSerializer(query,many=True).data
        return productos_serializado


class DetalleVentaProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model=SaleDetail
        fields=(
            'id',
            'sale',
            'product',
            'count',
            'price_purchase',
            'price_sale',
        )

    #