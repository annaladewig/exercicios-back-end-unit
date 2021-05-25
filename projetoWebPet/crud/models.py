from django.db import models

# Create your models here.

class Animals(models.Model):
    nome= models.CharField(
        max_length=255,
        null= False,
        blank= False
    )

    raca = models.CharField(
        max_length= 255,
        null= False,
        blank=False
    )

    especie = models.CharField(
        max_length= 255,
        null= False,
        blank=False
    )

    peso = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    dataNascimento = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    donoPet = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )


    telefone=models.CharField(
        max_length= 14,
        null= False,
        blank=False
    )

    endereco = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

