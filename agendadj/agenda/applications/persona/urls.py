from django.urls import path, re_path

from . import views

app_name='persona_app'

urlpatterns = [
    path(
        'persona/listar',
        views.ListaPersonasListView.as_view(),
        name='listar_personas'
    ),
    #CLASE 2020 JSON serializador
    path(
        'persona/listar/api/',
        views.PersonListApiView.as_view(),
        
    )
]