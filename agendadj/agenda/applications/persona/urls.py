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
        
    ),
    ##clase 223 CreateApiviews
    path("persona/registar",
    views.PersonCreateview.as_view(),
    name='registrar_persona_api'
    ),
    #clase 224 Obtener un registro en Api
    path(
        'persona/obtener/<pk>',
        views.PersonDetailsAPIviews.as_view(),
        name='obtener_persona'
    ),
    #clase 224 Eliminar registro por api
    path(
        'persona/eliminar/<pk>',
        views.PersonEliminarAPIviews.as_view(),
        name='eliminar_persona'
    ),
    #clase 225 actualizar
    path(
        "persona/actualizar/<pk>",
        views.PersonActualizaApiviews.as_view(),
        name="actualizar_registro"
    ),
    # clase 225 actualizar pero recuperando los datos
    path(
        "persona/actualizar/obtener/<pk>",
        views.PersonActualizaRetriveApiviews.as_view(),
        name="actualizar_registro_recuperando"
    ),
    
]