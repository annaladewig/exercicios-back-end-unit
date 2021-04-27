"""academiaBodyBuilder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
# O include permite que eu chame um app aqui na pasta de urls.

# Serve para direcionar para onde o usuário está indo de acordo com a URL que ele vai digitar.
# http://localhost:8000/clientes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls'))
    # Logo, quando o usuário digitar /clientes na url ele vai ser direcionado para o app de clientes.
    # E, dentro do app de clientes, ele vai ser direcionado para o arquivo de urls.
]
