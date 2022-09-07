#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
print('\033[33m ={:=^40} \033[m'.format(' CONTAGEM REGRESSIVA '))
for c in range(10, -1, -1):
    print('\033[36m {} \033[m'.format(c))
    sleep(1)
print('\033[33m-=\033[m' * 30)
print('\033[35mFOGOS\033[m')
print('\033[33m-=\033[m' * 30)
