# usuario/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Usamos la vista mágica de Django, solo le decimos qué HTML usar
    path('login/', auth_views.LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'), 
    path('registro/profesor/', views.registro_profesor, name='registro_profesor'),
    path('registro/alumno/', views.registro_alumno, name='registro_alumno'),
]