from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=("__all__")

# clase 226 Serializadores desconectados de modelos
class PersonaSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    full_name=serializers.CharField()
    job=serializers.CharField()
    email=serializers.EmailField()
    phone=serializers.CharField()
    #atributos pisiblemente no tengan todos los modelos
    activo = serializers.BooleanField(required=False)

#227 agregando atribustos a una clase
class PersonSerializer2(serializers.ModelSerializer):
    activo = serializers.BooleanField(required=False)
    class Meta:
        model=Person
        fields=("__all__")