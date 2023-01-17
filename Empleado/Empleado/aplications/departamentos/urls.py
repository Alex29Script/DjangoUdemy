#clase 61
from django.contrib import admin
from django.urls import path


from . import views



urlpatterns = [
    path(
        "departamento/nuevo",
        views.NewDepartamentoView.as_view(),
        name="nuevo_departamento"
        )
]