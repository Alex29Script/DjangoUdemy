from django.db import models

#257
class SalesDetailManager(models.Manager):
    
    def productos_por_venta(self,venta_id):
        consulta=self.filter(
            sale__id=venta_id
        ).order_by('count')
        return consulta