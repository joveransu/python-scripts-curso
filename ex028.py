#Escreva um programa que faça o computador 'Pensar' em um número inteiro entre 0 a 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador

from random import randint
from time import sleep
ale = randint(0,5)
print('~=~'*20)
print('Irei pensar em um número de 0 a 5, tente adivinhar!')
print('~=~'*20)
num = int(input('Que numero estou pensando? '))
print('PROCESSANDO...')
sleep(2)
if ale == num:
    print('Você ACERTOU.')
else:
    print('Você ERROU, número que pensei foi {}.'.format(ale))
