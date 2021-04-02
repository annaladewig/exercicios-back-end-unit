from django.shortcuts import render     #Possibilita a renderização de um arquivo .html
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from .models import Cliente
from rest_framework.status import HTTP_200_OK

# Create your views here.
def inicio(request):

    contexto = {
        'Nome': 'Anna Ladewig',
        'Endereco': 'Rua Tal',
        'Cidade': 'Recife'
    }

    return render(request, "inicio.html", contexto)

@csrf_exempt #traz a não obrigatoriedade de usar a proteção csrf
def cadastro(request):

    response = {}

    if request.method == 'POST':
        cliente = Cliente()
        cliente.nome = request.POST.get('nome') #o campo nome da tabela cliente vai receber a informação que está no campo nome do formulário html
        cliente.sobrenome = request.POST.get('sobrenome')
        cliente.cpf = request.POST.get('cpf')
        cliente.telefone = request.POST.get('telefone')
        cliente.save() #salva as informações no banco de dados

        #informa que deu tudo certo
        response = {
            'response': HTTP_200_OK
         }

    return HttpResponse(json.dumps(response))