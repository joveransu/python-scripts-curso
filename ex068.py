#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

print('\033[33m-=\033[m' * 20)
print('{:^20}'.format('VAMOS JOGAR PAR OU IMPAR?'))
print('\033[33m-=\033[m' * 20)

vitorias = 0
while True:
    pc = randint(0, 10)
    player = int(input('Que número você quer? '))
    resultado = 'PAR' if (pc + player) % 2 == 0 else 'IMPAR'

    res = str(input('Você deseja PAR ou IMPAR? [P/I] ')).upper().strip()[0]
    while not res in 'PI':
        res = str(input('Você deseja PAR ou IMPAR? [P/I] ')).upper().strip()[0]
    print('\033[33m-=\033[m' * 20)
    sleep(1)
    if (pc + player) % 2 == 0 and res == 'P':
        print(f'\033[32mVocê ganhou, digitou {player}, eu pensei no número {pc}, o total da {pc+player}, {resultado}\033[m')
        vitorias += 1
    elif (pc + player) % 2 == 1 and res == 'I':
        print(f'\033[32mVocê ganhou, digitou {player}, eu pensei no número {pc}, o total da {pc+player}, {resultado}\033[m')
        vitorias += 1
    else:
        print(f'\033[31mVocê perdeu, digitou {player}, eu pensei no número {pc}, o total da {pc+player}, {resultado}')
        break
print(f'GAME OVER. Você teve {vitorias} vitórias consecutivas.\033[m')
