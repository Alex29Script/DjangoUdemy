from rest_framework import serializers
from .models import Person, Hobby, Reunion

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

#228
from .models import Hobby

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model=Hobby
        fields=('__all__')

class PersonaSerializer3(serializers.ModelSerializer):
    
    #para campos ManyTo Many
    hobby=HobbySerializer(many=True)
    class Meta:
        model=Person
        fields=(
            'id',
            'full_name',
            'job',
            'email',
            'hobby'
        )

class ReunionSerializer(serializers.ModelSerializer):
    
    #para un llave foranea
    persona=PersonSerializer()# crea un json de la persona de la reunion con sus datos
    
    class Meta:
        model= Reunion
        fields=(
        'id','fecha','hora','asunto','persona'
        )

#clase 229 Metodos de un serializador
class ReunionSerializer2(serializers.ModelSerializer):
    
    #para un llave foranea
    #persona=PersonSerializer()# crea un json de la persona de la reunion con sus datos
    activo=serializers.BooleanField(default=False)
    # un campo que va ser caculado
    fecha_hora=serializers.SerializerMethodField()

    class Meta:
        model= Reunion
        fields=(
        'id','fecha','hora','asunto','persona', # se debe agregar aca
        "fecha_hora", "activo"
        )
    
    def get_fecha_hora(self,obj):
        return str(obj.fecha)+"T"+str(obj.hora)

#Clase 230 LinkSerializer para obtener link en vez de datos
# en los campos realacionados.

class ReunionSerializer230(serializers.HyperlinkedModelSerializer):
    activo=serializers.BooleanField(default=False)
    # un campo que va ser caculado
    fecha_hora=serializers.SerializerMethodField()

    class Meta:
        model= Reunion
        fields=(
        'id','fecha','hora','asunto','persona', # se debe agregar aca
        "fecha_hora", "activo"
        )
        
        extra_kwargs={
        'persona':{'view_name':'persona_app:detalle','lookup_field':'pk'}
        }
    
    def get_fecha_hora(self,obj):
        return str(obj.fecha)+"T"+str(obj.hora)

# 231 Paginacion en serializadores
from rest_framework import pagination
class PersonPagination(pagination.PageNumberPagination):
    page_size=2 #carga en pagina
    max_page_size=100 # carga en memoria