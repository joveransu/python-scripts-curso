#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))

print(f'Numeros gerados foram: {numeros}')
print(f'{sorted(numeros)[0]} é o menor numero da lista.')
#print(f'O menor valor foi {min(numeros)}')
print(f'{sorted(numeros)[-1]} é o maior numero da lita.')
#print(f'O menor valor foi {max(numeros)}')