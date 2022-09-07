#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

num = list()
for c in range(0, 5):
    num.append(int(input(f'Digite um número na posição {c}: ')))

print(f'Você digitou os valores {num}')

helped = num.copy()
helped.sort()

menor_valor = helped[0]
print(f'O menor valor foi {menor_valor} na posição: ', end='')
for c, v in enumerate(num):
    if v == menor_valor:
        print(f'{c}...', end='')

maior_valor = helped[-1]
print(f'\nO maior valor foi {maior_valor} na posiçaõ: ', end='')
for c, v in enumerate(num):
    if v == maior_valor:
        print(f'{c}...', end='')

