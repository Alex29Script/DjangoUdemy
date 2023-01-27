from django.db import models

class ProductoUsuarioManager(models.Manager):

    def producto_por_user(self,usuario):
        return self.filter(
            user_created=usuario,
        )