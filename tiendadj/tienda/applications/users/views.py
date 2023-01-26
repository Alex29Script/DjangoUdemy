from django.shortcuts import render
from .models import User
# Create your views here.

#242  
from firebase_admin import auth


#clase 236 codigo para auth con google
from django.views.generic import TemplateView

class loginTemplateView(TemplateView):
    template_name='users/236login.html'

#240 Vista del token
from rest_framework.views import APIView
from .serialiazers import LoginGoogleSerializers

##244 importando
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class GoogleLoginView(APIView):
    serializer_class=LoginGoogleSerializers
    
    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        id_token=serializer.data.get('token_id')
        #print('####### 1 #############')
        #print(id_token)
        #241 tomar el token y desecriptarlo
        # firebase para python https://firebase.google.com/docs/admin/setup?authuser=0&hl=es#python
        # 242 obteniendo la credenciales
        # obtener credenciales https://console.firebase.google.com/u/0/project/djangoventasudemy/settings/serviceaccounts/adminsdk
        # modifica el archivo local de settings para agregarlo al proyecto

        #243 Decodificar el token obteniedo los datos
        decode_token=auth.verify_id_token(id_token)
        #print("#######", decode_token)
        email=decode_token['email']
        name=decode_token['name']
        avatar=decode_token['picture']
        verified=decode_token['email_verified']
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$  objetos:", email,name,avatar)
        usuario, created=User.objects.get_or_create(
            email=email,
            defaults={
                "full_name":name,
                "email":email,
                "is_active":True
            }
        )
        print("user:", usuario)
        print("created:", created)

        #244 Creando Token en Django
        if created==True:
            token=Token.objects.create(user=usuario)
        else:
            token=Token.objects.get(user=usuario)
        print("_______________________________",token)
        userGet={
            "id":usuario.pk,
            'email':usuario.email,
            "full_name":usuario.full_name,
            "genero":usuario.genero,
            "date_birth":usuario.date_birth,
            "city":usuario.city
        }
        print("####  Ultimo    ############")

        return Response(
            {
                'token':token.key,
                'user':userGet
            }
        )