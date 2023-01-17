#clase 56 Formularios y su edicion
#creacion del archivo form.py

#clase 57 Formularios Django
from django import forms

from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Prueba
        fields = ('titulo','subtitulo','cantidad')
        #clase 59 Personalizar Formularios o campos
        widgets={
            "titulo":forms.TextInput(
                attrs={ # attrs representan los atributos en html
                    'placeholder':"ingrese el titulo aqui"
                }
            )
        }
    #clase 58 validaciones formulario
    def clean_cantidad(self):
        cantidad=self.cleaned_data['cantidad']
        if cantidad<10:
            raise forms.ValidationError('ingrese un numero mayor a 10')
        return cantidad

