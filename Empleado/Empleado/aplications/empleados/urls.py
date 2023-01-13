from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ListarEmpleados',views.ListAllEmpleados.as_view()),
    ##clase37
    ##path("listaEmpleadosByDepartamentos", views.ListByAreaEmpleado.as_view())
    ##clase 38
    path("listaEmpleadosByDepartamentos/<shorname>/", views.ListByAreaEmpleado.as_view())
]