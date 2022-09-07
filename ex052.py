#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
contador = 0
for c in range(1,10):
    if c == n and c != 1:
        contador = contador
    elif n % c == 0:
        contador += 1
if contador == 1:
    print('É primo.')
else:
    print('Não é primo.')