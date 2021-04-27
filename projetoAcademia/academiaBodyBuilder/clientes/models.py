from django.db import models

# Create your models here.
# Aqui você vai criar aquilo que representa as suas tabelas pro Banco de Dados.
# Para cada classe a gente tem uma tabela.

class Cliente(models.Model):

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

    telefone = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )