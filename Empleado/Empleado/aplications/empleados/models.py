from django.db import models
from Empleado.aplications.departamentos.models import Departamento

JOB_CHOICES=(
    ("0","Contador"),
    ("1","Administrador"),
    ("2","Economista"),
    ("3","OTRO"),
)
# Create your models here.
class Empleado(models.Model):
    firs_name = models.CharField("Nombres", max_length=60)
    last_name = models.CharField("Apellidos", max_length=60)
    job = models.CharField("Trabajo",choices=JOB_CHOICES, max_length=10)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #image = models.ImageField("Foto", upload_to=None, height_field=None, width_field=None, max_length=None)
    
    def __str__(self):  
        return str(self.id)+" "+self.firs_name+" "+self.last_name+" "+self.job+" "+str(self.departamento)
    