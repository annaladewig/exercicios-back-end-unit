from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Animals


def index(request):#Ação que renderiza a view início, consulta  os dados no banco, empacota e envia para template início

    animals = Animals.objects.all() #Fazendo o select * from


    contexto ={
        'animals': animals
    }

    return render(request, 'index.html', contexto)


def create(request):
    response = {} #inicializando o dicionário

    if request.method == 'POST':
        animals = Animals()
        animals.nome = request.POST.get('nome') #esse request.POST.get vai pegar o dado do campo nome do formulário, e colocar no campo da tabela nome da tabela cliente
        animals.raca = request.POST.get('raca')
        animals.especie = request.POST.get('especie')
        animals.peso = request.POST.get('peso')
        animals.dataNascimento = request.POST.get('dataNascimento')
        animals.donoPet = request.POST.get('donoPet')
        animals.telefone = request.POST.get('telefone')
        animals.endereco = request.POST.get('endereco')
        animals.save()

    return HttpResponseRedirect('/crud/index')



def create_template(request):
    return render(request,'create.html')

def read(request, user_id):
    if request.method == 'GET':
        animal = Animals.objects.filter(id=user_id) #aqui vai filtrar uma ou mais
        contexto = {
            'animals': animal

        }
        return render(request, 'read.html', contexto)

def update_template(request, user_id): #Ação que renderiza a view atualizar, consulta  os dados no banco, empacota e envia para view
    if request.method == 'GET':
        animal = Animals.objects.filter(id=user_id)
        contexto = {
            'animal': animal #cliente recuperado do banco de dados que tem o user_id

        }
        return render(request, 'update.html', contexto)

def update(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        nome = request.POST.get('nome')
        raca = request.POST.get('raca')
        especie = request.POST.get('especie')
        peso = request.POST.get('peso')
        dataNascimento = request.POST.get('dataNascimento')
        donoPet = request.POST.get('donoPet')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')


        cliente = Animals.objects.filter(id=user_id)
        cliente.update(nome=nome, raca=raca, especie=especie, peso=peso, dataNascimento= dataNascimento, donoPet= donoPet, telefone=telefone, endereco=endereco )

        return HttpResponseRedirect('/crud/index')


def delete(request, user_id):
    if request.method == 'GET':
        animal = Animals.objects.filter(id=user_id) #aqui vai filtrar uma ou mais
        animal.delete()

        return HttpResponseRedirect('/crud/index')


def home(request):
    return render(request, 'home.html')

def criadores(request):
    return render(request, 'criadores.html')

def social(request):
    return render(request, 'social.html')
