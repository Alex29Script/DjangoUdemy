from django.urls import path

from . import views

app_name='users_app'

urlpatterns = [
    #236 login
    path(
        'login/',
        views.loginTemplateView.as_view(),
        name='login'
    )
]