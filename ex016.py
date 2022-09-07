#https://www.python.org

#import math
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
#print('A raiz de {} é igual a {}'.format(num,math.ceil(raiz)))

#from math import sqrt, floor
#raiz = sqrt(num)
#print('A raiz de {} é igual a {}'.format(num, floor(raiz)))

#import random
#num = random.random()
#num2 = random.randint(1, 100)
#print(num, num2)

from math import floor, trunc
n = float(input('Digite um número: '))
print('Numero digitado {}, numero inteiro {}!'.format(n, floor(n)))
print('Numero digitado {}, numero inteiro {}!'.format(n, trunc(n)))
