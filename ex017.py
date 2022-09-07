#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

import math
co = float(input('Diga o tamanho do cateto oposto: '))
ca = float(input('Diga o tamanho do cateto adjacente: '))
#h = ((co**2) + (ca**2)) ** (1/2) # raiz quadrada da soma dos catetos elevado a 2 é o tamanho da hipotenusa
h = math.hypot(co,ca) # Usando a biblioteca de matematica
print('A hipotenusa é equivalente a {:.2f}.'.format(h))
