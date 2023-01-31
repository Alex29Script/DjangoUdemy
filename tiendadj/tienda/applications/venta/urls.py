from django.urls import path

from . import views


app_name="venta_app"


urlpatterns = [
    #256
    path(
        'venta/reporte/',
        views.ReporteVentasList.as_view(),
        name='reporte_venta'
    ),
    #259 registar venta
    path(
        'venta/registrar/',
        views.RegistroVentaApiViews.as_view(),
        name='registrar_venta'
    )
]

