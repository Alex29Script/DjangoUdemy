from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path("lista/prueba", views.ListarPruebas.as_view()),
    path(#clase 56 Formularios Django
        'addprueba',
        views.PruebaCreateView.as_view()
    ),
    path(
        'home/grillas',
        views.GrillasTemplateView.as_view()
        )    
]