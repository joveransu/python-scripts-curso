#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ang = float(input('Digite o valor do ângulo: '))
ang = math.radians(ang) # O Angulo precisa ser convertido para radianos.
print('Valor digitado foi {:.2f}.\nSeno é {:.2f}.\nCosseno é {:.2f}.\nTangente é {:.2f}.'.format(ang, math.sin(ang), math.cos(ang), math.tan(ang)))
