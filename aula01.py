print("Hello World")

#Variáveis em Python
print('# Variáveis em Python #')

a = 1 #inteiro
b = 'texto' #string
c = 1.5 #float
d = [1,5,6,7, "texto"] #lista

print(d)
type(a) #diz qual o tipo da variável


#Imprimir na Tela
print('# Imprimir na Tela #')

print("Olá!")

str_teste = "Meus estudos Python!"
print(str_teste)

print(str_teste * 20) #Imprime na tela 20 vezes


#Operações Matemáticas
print('# Operações Matemáticas #')

soma = 5 + 7
multiplicacao = 5 * 6
divisao = 5 / 7
resto_divisao = 7 % 11
elevacao_potencia = 3 ** 2
print('Soma', soma, '| Multiplicação: ', multiplicacao, '| Divisão: ', divisao, '| Resto da divisão ', resto_divisao, '| Elevação à Potência: ', elevacao_potencia)


#Expressões Lógicas
print('# Expressões Lógicas #')
if 4 == 4 and 5 == 5:
    print('Ok')

if 4 == 4 or 5 == 5:
    print('print')

if 4 != 5 and 5 <= 10:
    print("Verdadeiro")

if 7 in d:
    print("Temos o valor 7 na lista d.")
else:
    print("Não temos o valor desejado na lista d.")

if 10 not in d:
    print("O valor desejado não está na lista.")
else:
    print("O valor desejado está na lista.")


# Conversões
print('# Conversões #')

print(int(5.2)) #Converte de float para inteiro
print(float(8)) #Converte de inteiro para float


# Input
print('# Input #')

valor_digitado = input('Digite o valor a ser buscado:')

if int(valor_digitado) in d:
    print("O valor ", valor_digitado," está na lista.")
elif valor_digitado.isdigit():
    print("O valor digitado é um dígito.")
else:
     print("O valor ", valor_digitado," não está na lista.")


#Listas, Tuplas e Dicionários
print('# Listas, Tuplas e Dicionários #')

#A lista pode ser alterada

lista = [5,6,7,98,100]  #Valores dentro de um colchete
print(lista)

#A tupla não pode ser alterada

tupla = (5,1,8,6,4,7,5)  #Valores dentro de parênteses
print(tupla)

#O dicionário é um conjunto de chave valor, você consegue indexar pela chave.

dicionario = {
    'item_1': 10,
    'item_2': 20,
    'item_3': 30,
    'item_5': [5,6,7,98,100],
    'item_4': {   #Um dicionário dentro de outro dicionário
        'item_01'
    }
}
print(dicionario)

dicionario_2 = {}
dicionario_2['chave_1'] = 'valor'
dicionario_2['chave_2'] = 59

print(dicionario_2)

# Outro Exemplo utilizando Dicionário

Grunt = {'Categoria':'Guerreiro', 'força':110, 'experiencia':50, 'vida':100, 'Cura':70}
Shallur = {'Categoria':'Mago', 'força':50, 'experiencia':120, 'vida':60, 'Cura':100}
Eldor = {'Categoria':'Elfo', 'força':70, 'experiencia':80, 'vida':120, 'Cura':110}
Kallipha = {'Categoria':'Mago', 'força':70, 'experiencia':100, 'vida':80, 'Cura':90}

print ('Categoria de Kallipha =', Kallipha['Categoria'])
print('Força de Grunt = ', Grunt['força'])

Kallipha["categoria"] = 'elfo'
Grunt['Armas'] = ['escudo', 'espada']

print ('Categoria de Kallipha =', Kallipha['Categoria'])
print('Força de Grunt = ', Grunt['Armas'])


#Laços de Repetição
print('# Laços de Repetição #')

list_range = range(5,10) #Diz que eu quero um intervalo entre 5 e 10
print(list(list_range))

list_range2 = range(5)

print(" ")

for value in list_range: #Percorre o array
    print(value)

print(" ")

for value in list_range2: #Percorre o array
    print(value)

array_str = ['aula 1','aula 2','aula 3','aula 4']
print(array_str)

dicionario_de_aulas = {}

for value in array_str:
    dicionario_de_aulas[value] = 30

print(dicionario_de_aulas)

var_start_value = 10

for value in array_str:
    dicionario_de_aulas[value] = var_start_value
    var_start_value +=10

print(dicionario_de_aulas)

conteudos_possiveis = ['logica_de_programacao', 'java_para_iniciantes', 'android_inicio', 'python_para_web']
dicionario_conteudo_aulas = {}

for count, value in enumerate (array_str):
    dicionario_conteudo_aulas[value] = conteudos_possiveis[count]

print(dicionario_conteudo_aulas)


contador = 1
while contador < 15:
    print(contador)
    contador = contador + 1
else:
    print('Loop finalizado')


for disc in lista:
    print(disc)
