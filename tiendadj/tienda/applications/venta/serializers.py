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
            #257
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

# 258 Registrar venta
#serializador 

class ProductDetailSerializers(serializers.Serializer):
    
    pk=serializers.IntegerField()
    count=serializers.IntegerField()

class ProcesoVentaSerializer(serializers.Serializer):

    #contruyendo las key del serializador
    #campos necesarios del froned
    type_invoce=serializers.CharField()
    type_payment=serializers.CharField()
    adreese_send=serializers.CharField()
    #Detalle de la venta
    productos=ProductDetailSerializers(many=True)
    

