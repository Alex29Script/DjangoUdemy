from django.urls import path, re_path, include

from . import views



app_name='productos_app'

urlpatterns = [
    path(
        'productos/listar/todos',
        views.ListaProductosApiView.as_view(),
        name='listar_todos_productos'
    ),
]