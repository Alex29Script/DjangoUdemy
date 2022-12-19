from django.urls import path
from . import views

urlpatterns = [
    path("administrador/prueba", views.admin_prueba_app.as_view())
]