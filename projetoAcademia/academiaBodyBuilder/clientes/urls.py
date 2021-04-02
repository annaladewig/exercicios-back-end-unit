from django.urls import path, include
from . import views

#http://localhost:8000/clientes/inicio
#http://localhost:8000/clientes/cadastro

app_name = 'clientes'

urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('cadastro', views.cadastro, name='cadastro')
]