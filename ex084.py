"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

pessoas = list()
dados = list()
minimo = maximo = 0

while True:
    dados.append(str(input('Qual seu nome? ')).strip())
    dados.append(float(input('Qual seu peso? ')))
    if len(pessoas) == 0:
        minimo = maximo = dados[1]
    else:
        if dados[1] < minimo:
            minimo = dados[1]
        elif dados[1] > maximo:
            maximo = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    res = input('Quer continuar? [S/N]').strip()[0]
    if res in 'Nn':
        break

print(f'Fora cadastradas {len(pessoas)} pessoas.')
print(f'Peso minimo foi de {minimo}Kg que foram: ', end='')
for data in pessoas:
    if data[1] == minimo:
        print(f'{data[0]} ',end='')

print(f'\nPeso máximo foi de {maximo}Kg que foram: ', end='')
for data in pessoas:
    if data[1] == maximo:
        print(f'{data[0]} ',end='')