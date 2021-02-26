from django.db import models

# Create your models here.
# Comandos: python manage.py makemigrations -> cria o arquivo que vai criar as tabelas no banco (ex.: 0001_initial.py) e cria as tabelas de autenticação, permissão, etc. Ele também verifica se tem atualizações.
#           python manage.py migrate -> cria o banco. (o link com o Banco está em DATABASES no arquivo settings.py dentro de helloDjango.

class Funcionario(models.Model):
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    tempo_servico = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    remuneracao = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )
