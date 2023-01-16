from django.db import models
from Empleado.aplications.departamentos.models import Departamento

#app de teceros https://django-ckeditor.readthedocs.io/en/latest/#usage 
#clase 34
#para subir archivos a Django
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad=models.CharField("Habilidad", max_length=50)
    
    class Meta:
        verbose_name="Habilidad"
        verbose_name_plural="Habilidades de los Empleados"

    def __str__(self):
        return str(self.id)+" "+self.habilidad


JOB_CHOICES=(
    ("0","Contador"),
    ("1","Administrador"),
    ("2","Economista"),
    ("3","OTRO"),
    ("4", "Gerente"),
    ("5", "Operario")
)
# Create your models here.
class Empleados(models.Model):
    first_name = models.CharField("Nombres", max_length=60)
    last_name = models.CharField("Apellidos", max_length=60)
    full_name=models.CharField("Nombre Completo",max_length=120,blank=True)
    job = models.CharField("Trabajo",choices=JOB_CHOICES, max_length=10)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="empleado", blank=True,null=True)
    habilidades= models.ManyToManyField(Habilidades)
    #app de terceros clase 34 agrega editor html skeditor
    hoja_vida= RichTextField()

    #apliando un buscador clase 32
    search_fields=("first_name",)

    class Meta:
        verbose_name="Mi Empleado"
        verbose_name_plural="Empleados de la empresa"
        ordering=["first_name","last_name"]
        unique_together=("first_name", "departamento")
    
    def __str__(self):  
        return str(self.id)+" "+self.first_name+" "+self.last_name+" "+self.job+" "+str(self.departamento)



