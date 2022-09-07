"""
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,  mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

numlist = list()
res = 'S'
while res != 'N':
    numlist.append(int(input('Digite um número: ')))
    res = input('Quer continuar? [S/N]').strip().upper()[0]

numlist.sort(reverse=True)
print(f'Foram digitados {len(numlist)} números.')
print(f'Lista em ordem decrescente: {numlist}')
print('O 5 está na lista.' if 5 in numlist else 'O 5 não está na lista.')