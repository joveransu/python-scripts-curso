#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lop = int(input('Quantos palpites deseja? '))
start = 0
mainlist = list()
helpedlist = list()

while True:
    for c in range(0, 6):
        ale = randint(0, 60)
        while not ale in helpedlist and len(helpedlist) < 6:
            helpedlist.append(ale)
            ale = randint(0, 60)
        helpedlist.sort()


    print(f'Jogo {start+1}: {helpedlist}')
    sleep(1)
    mainlist.append(helpedlist[:])
    helpedlist.clear()
    start += 1
    if start == lop:
        break

        


    
