'''#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

print('='*40)
print('{: ^40}'.format(' LOJA SUPER BARATÃO '))
print('='*40)
total = caro = cont = valor = 0
namP = ' '
while True:
    nome = str(input('Nome do produto: ')).strip()
    preço = float(input('Qual valor? '))
    if cont == 0 or preço < valor:
        nameP = nome
        valor = preço
    total += preço
    if preço > 1000:
        caro += 1
    cont += 1
    res = ' '
    while not res in 'SN':
        res = str(input('Quer continuar? [S/N]')).strip().upper()
    if res == 'N':
        break
print('='*20)
print('Compras feitas.')
print(f'Total da compra foi R$:{total:.2f}.')
print(f'Tivemos {caro} produtos custando acima de R$ 1000,00')
print(f'O produto mais barato foi {nameP} que custava R$:{valor}')
print('='*20)