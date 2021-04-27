from django.shortcuts import render     #Possibilita a renderização de um arquivo .html
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
import json
from .models import Cliente
from rest_framework.status import HTTP_200_OK

# Create your views here.
# Aqui vão estar as funções que representam a sua regra de negócio.
# O arquivo urls sempre vai direcionar para o arquivo de views.

# O parâmetro, das funções que estão na view, SEMPRE será request. Pois recebem informação de uma url.
def inicio(request):

    clientes = Cliente.objects.all()
    contexto = {
        'clientes': clientes
    }

    return render(request, 'inicio.html', contexto)


def form_cadastro(request):
    return render(request, 'cadastro_db.html') # Carrega o arquivo HTML


def visualizar(request, user_id):
    if request.method == 'GET':
        cliente = Cliente.objects.filter(id=user_id)
        contexto = {
            'cliente': cliente
        }
    return render(request, "visualizar.html, contexto") # Carrega o arquivo HTML

def deletar(request, user_id):

    if request.method == 'GET':
        cliente = Cliente.objects.filter(id=user_id)
        cliente.delete()
    return HttpResponseRedirect('clientes/inicio')

#@csrf_exempt #traz a não obrigatoriedade de usar a proteção csrf (que é um proteção contra falsificação de solicitação de site cruzado)
def cadastro(request):

    response = {}

    if request.method == 'POST':
        cliente = Cliente() # a variável cliente recebe a classe Cliente que foi importada do models. (Instanciação)
        cliente.nome = request.POST.get('nome') # o campo nome da tabela cliente vai receber a informação que está no campo nome do formulário html.
        cliente.sobrenome = request.POST.get('sobrenome')
        cliente.cpf = request.POST.get('cpf')
        cliente.telefone = request.POST.get('telefone')
        cliente.save() # salva as informações no banco de dados

        # informa que deu tudo certo
        response = {
            'response': HTTP_200_OK
         }

    # O retorno tem que ser uma resposta do tipo HTTP. O Django só é capaz de exibir em uma página se for assim.
    return HttpResponse(json.dumps(response))