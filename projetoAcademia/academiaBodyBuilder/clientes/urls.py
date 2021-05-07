from django.urls import path, include
from . import views
# O . é porque vai ser feita uma importanção dentro do mesmo diretório.
# Com essa importação, esse meu arquivo de ulrs consegue enxergar o arquivo views.py.

# http://localhost:8000/clientes/inicio
# http://localhost:8000/clientes/cadastro

app_name = 'clientes'
# O Djando, sempre que chega no arquivo de urls, ele verifica o nome do app.

# Aqui temos a url de caminhos, que vai ter por objetivo levar o usuário até as views.
# É uma variável que vai conter uma lista.
urlpatterns = [
    # Vai direcionar para o arquivo de views, para a função início desse arquivo.
    path('inicio', views.inicio, name='inicio'),
    path('cadastro', views.cadastro, name='cadastro'),

    path('form_cadastro', views.form_cadastro, name="form_cadastro"),
    path('visualizar/<int:user_id>', views.visualizar, name="visualizar"),
    path('deletar/<int:user_id>', views.deletar, name="deletar"),
    path('atualizar/<int:user_id>', views.atualizar, name="atualizar"),
    path('atualizar_dados_usuario', views.atualizar_dados_usuario, name="atualizar_dados_usuario"),

]