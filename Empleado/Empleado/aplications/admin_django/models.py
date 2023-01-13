from django.db import models

# Create your models here.

class Admin_Modelo(models.Model):
    name = models.CharField("Nombre", max_length=50)
    shor_name = models.CharField("Nombre Corto", max_length=20, unique=True)
    anulate = models.BooleanField("Anulado",default=False)
    

    ##estilos
    class Meta:
        verbose_name="Mi Departamento" # mostrar en el admin    
        verbose_name_plural="Areas de la empresa" #para los plurales
        ordering=["name"] #ordenar por nombre
        unique_together=("name", "shor_name") # unicos archivos al hacer una combinacion entre las dos propiedades
    

    def __str__(self):
        return str(self.id)+" - "+ self.name +" - "+self.shor_name