from django.db import models

class ProductoUsuarioManager(models.Manager):

    def producto_por_user(self,usuario):
        return self.filter(
            user_created=usuario,
        )

    def productos_con_stock(self):
        return self.filter(
            stok__gt=0 # productos con stock
        ).order_by('-num_sales')

    #254    

    def producto_por_genero(self,genero):
        # lista productos por genero
        if genero=='m':
            mujer=True
            varon=False
        elif genero=='v':
            mujer=False
            varon=True
        else:
            varon=True
            mujer=True

        return self.filter(
            woman=mujer,
            man=varon
        ).order_by('created')

    # 255 filtros por parametros
    def filtrar_productos_parametros(self, **filtros):
        return self.filter(
            man=filtros['man'],
            woman=filtros['woman'],
            name__icontains=filtros['name'] # se paresca o contenga
        )