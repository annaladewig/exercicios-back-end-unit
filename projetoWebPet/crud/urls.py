from django.urls import path, include
from . import views, admin

app_name='crud'

urlpatterns = [
    path('index', views.index, name='index'),
    path('create_template', views.create_template, name='create_template'), #Será o nosso formulário
    path('create', views.create, name='create'),
    path('read/<int:user_id>', views.read, name="read"),  # esse link vai ser aberto pelo id
    path('update_template/<int:user_id>', views.update_template, name="update_template"),
    path('update', views.update, name="update"),
    path('delete/<int:user_id>', views.delete, name="delete"),
    path('home', views.home, name="home"),
    path('criadores', views.criadores, name="criadores"),
    path('social', views.social, name="social"),

]