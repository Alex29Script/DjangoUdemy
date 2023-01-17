from django.contrib import admin
from django.urls import path
from . import views


#clase 48
app_name="empleados_app"


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
    #clase 45
    path("CrearEmpleado", views.EmpleadoCreateView.as_view()),
    #clase 47
    #path("success", views.SuccessView.as_view())
    #clase 48
    path("success", views.SuccessView.as_view(), name="correcto"),
    #clase51 Updateviews
    path(
        "ActualizarEmpleado/<pk>",
        views.EmpleadosUpdateView.as_view(),
        name="actualizar_empleado"
    ),
    path(
        "eliminar/<pk>/",
        views.EliminarEmpleadoDeleteView.as_view(),
        name="eliminar_empleado"
        
        )
]