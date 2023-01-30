from django.urls import path, re_path, include

from . import views



app_name='productos_app'

urlpatterns = [
    path(
        'productos/listar/todos',
        views.ListaProductosApiView.as_view(),
        name='listar_todos_productos'
    ),
    #254
    path(
        'productos/genero/<genero>',
        views.ListaProductosGeneroApiView.as_view(),
        name='listar_todos_productos_genero'
    ),
    #255
    path(
        'productos/3filtros/',
        views.FiltrarProductosParametrosAPIView.as_view(),
        name='listar_todos_productos_parametros'
    )
]