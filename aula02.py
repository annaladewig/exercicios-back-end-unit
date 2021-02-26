#Funções

def calcMedia(lista: list):
    somatorio = 0
    for value in lista:
        somatorio += value

    media = somatorio/len(lista)

    return media

preco_carros = [50000,30000,2500,36000,86000,70000]
media_preco_carros = calcMedia(preco_carros)

print('A média de preço de carros é: ', media_preco_carros)