from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField("Nombre", max_length=50)
    shor_name = models.CharField("Nombre Corto", max_length=20, unique=True)
    anulate = models.BooleanField("Anulado",default=False)
    
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/
    # no hay necesidad de especificar id, pero el mismo esta creando id

    class Meta:
        verbose_name="Mi Departamento"   
        verbose_name_plural="Areas de la empresa" 
        ordering=["name"] 
        unique_together=("name", "shor_name") 

    def __str__(self):
        return str(self.id)+" - "+ self.name +" - "+self.shor_name