# Faça um programa que peça as 4 notas bimestrais e mostre a média:

n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))
n3 = float(input('Digite o terceiro número:'))
n4 = float(input('Digite o quarto número:'))

total = (n1 + n2 + n3 + n4)/4
print('\nA média dos números é: {}\n'.format(total))

# Faça um programa que converta metros para centímetros:

metros = float(input('\nDigite um número:'))

centimetros = metros * 100

print('\nO valor {} em centímetros é: {} centímetros.'.format(metros, centimetros))

"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa
deve calcular a média alcançada por aluno e apresentar:
• A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
• A mensagem "Reprovado", se a média for menor do que sete;
• A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nota1 = input('\nDigite a primeira nota: ')
nota2 = input('Digite a segunda nota: ')

nota1 = float(nota1)
nota2 = float(nota2)

media = (nota1 + nota2) / 2

if 7 <= media < 10:
    print('APROVADO')
elif media < 7:
    print('REPROVADO')
else:
    print('APROVADO COM DISTINÇÃO')

"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de
Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS
corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido
corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a
quantidade de horas trabalhadas no mês.
• Desconto do IR:
• Salário Bruto até 900 (inclusive) - isento
• Salário Bruto até 1500 (inclusive) - desconto de 5%
• Salário Bruto até 2500 (inclusive) - desconto de 10%
• Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo
abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""



"""
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a
metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi
contratado para desenvolver o programa que monta a tabela de preços de pães,
de 1 até 50 pães, a partir do preço do pão informado pelo usuário.
"""

qtd_paes = int(input('\nDigite a quantidade de pães: '))

while qtd_paes > 50:
    qtd_paes = int(input('Digite a quantidade de pães [Menos que 50]: '))

preco_pao = float(input('Qual é o preco do pao? R$ '))

for cont, i in enumerate(range(qtd_paes)):
    if cont > 0:
        preco_pao_qtd = preco_pao * cont
        print(cont, ' = R$ ', preco_pao_qtd)