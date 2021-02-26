from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import HTTP_200_OK
from.models import Funcionario
import json

# Create your views here.
def inicio(request):

    dados_usuario = {
        'nome_pessoa': 'João Alves Silva',
        'endereco_pessoa': 'Rua 12',
        'ciadade_pessoa': 'Recife'
    }
    return HttpResponse(json.dumps(dados_usuario)) # transforma o dicionário em json

@csrf_exempt   #O Django exige esse token por questão de segurança.
def cadastro_usuario(request):

    response = {}  # declara um dicionário
    if request.method == 'POST':

        funcionario = Funcionario() # instancia um objeto da classe Funcionario
        funcionario.nome = request.POST.get('nome')
        funcionario.sobrenome = request.POST.get('sobrenome')
        funcionario.cpf = request.POST.get('cpf')
        funcionario.tempo_servico = request.POST.get('tempo_servico')
        funcionario.remuneracao = request.POST.get('remuneracao')
        funcionario.save()  # Salva no Banco de dados

        response = {
            'response': HTTP_200_OK  # O código HTTP 200 OK é a resposta de status de sucesso que indica que a requisição foi bem sucedida.
        }
    return HttpResponse(json.dumps(response))