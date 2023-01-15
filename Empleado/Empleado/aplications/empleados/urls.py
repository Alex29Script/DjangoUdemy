from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ListarEmpleados/',views.ListAllEmpleados.as_view()),
    ##clase37
    ##path("listaEmpleadosByDepartamentos/", views.ListByAreaEmpleado.as_view())
    ##clase 38
    path("listaEmpleadosByDepartamentos/<shorname>/", views.ListByAreaEmpleado.as_view()),
    #clase 39
    path("listarEmpleadosKwords/", views.ListEmpleadosByKword.as_view()),
    #clase 42 listar habilidades de un empleado
    path("habilidadesEmpleado/", views.ListHabilidadesEmpleado.as_view()),
    
    
    #clase 43 Dailviews pk hacer referencia al id
    path("DetalleEmpleado/<pk>/", views.EmpleadoDetailView.as_view()),

]