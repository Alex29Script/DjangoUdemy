from django.urls import path

from . import views

app_name='users_app'

urlpatterns = [
    #236 login
    path(
        'login/',
        views.loginTemplateView.as_view(),
        name='login'
    ),
    path(
        'api/google/login/',
        views.GoogleLoginView.as_view(),
        name='login_google'    
    )
]