from . import views
from django.urls import path, include

app_name = 'usuarios'

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),  # vai para função início, dentro do arquivo views.py
    path('cadastro_usuario', views.cadastro_usuario, name='cadastro_usuario')  # vai para função cadastro_usuario, dentro do arquivo views.py
]