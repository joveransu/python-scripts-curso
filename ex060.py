#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número para saber seu fatorial: '))
fatorial = 1
while num > 1:
    print('{} => '.format(num), end='')
    fatorial *= num
    num -= 1
    if num <= 1:
        print('=> 1\nSeu fatorial é {}.'.format(fatorial))

from math import factorial
num = int(input('Digite um número para saber seu fatorial: '))
print('O fatorial de {}, é {}'.format(num, factorial(num)))