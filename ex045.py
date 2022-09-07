#Crie um programa que faça o computador jogar Jokenpô com você.

'''from random import randint

print('\033[33m-=\033[m' * 20)
print(' ' * 15 + '\033[32mJOKENPÔ\033[m')
print('\033[33m-=\033[m' * 20)

choose = int(input('Escolha: (1 = Pedra, 2 = Papel, 3 = Tesoura) '))
print('\033[33m-=\033[m' * 20)
maquina = randint(1,3)

if choose == maquina:
    print('\033[33mEMPATE\033[m')
elif choose == 1 and maquina == 2 or choose == 2 and maquina == 3 or choose == 3 and maquina == 1:
    print('\033[31mVOCÊ PERDEU\033[m')
else:
    print('\033[34mVOCÊ GANHOU\033[m')

if maquina == 1:
    maquina = 'Pedra'
elif maquina == 2:
    maquina = 'Papel'
else:
    maquina = 'Tesoura'

if choose <= 1:
    print('Sua escolha \033[33mPedra\033[m Vs \033[33m{}.\033[m'.format(maquina))
elif choose == 2:
    print('Sua escolha \033[33mPapel\033[m Vs \033[33m{}.\033[m'.format(maquina))
else:
    print('Sua escolha \033[33mTesoura\033[m Vs \033[33m{}.\033[m'.format(maquina))
    
print('\033[33m-=\033[m' * 20)
'''


from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('\033[33m-=\033[m' * 20)
print(' ' * 15 + '\033[32mJOKENPÔ\033[m')
print('\033[33m-=\033[m' * 20)
print('''Escolha uma opção:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual sua jogada? '))
print('\033[33m-=\033[m' * 20)
print('\033[36mJO...')
sleep(0.5)
print('..KEN..')
sleep(0.5)
print('..PÔ!\033[m')
sleep(0.5)
print('\033[33m-=\033[m' * 20)
if computador == 0:
    if jogador == 0:
        print('\033[33mEMPATE\033[m')
    elif jogador == 1:
        print('\033[34mVOCÊ GANHOU\033[m')
    elif jogador == 2:
        print('\033[31mVOCÊ PERDEU\033[m')
    else:
        print('\033[31mJogada inválida\033[m')
elif computador == 1:
    if jogador == 0:
        print('\033[31mVOCÊ PERDEU\033[m')
    elif jogador == 1:
        print('\033[33mEMPATE\033[m')
    elif jogador == 2:
        print('\033[34mVOCÊ GANHOU\033[m')
    else:
        print('\033[31mJogada inválida\033[m')
elif computador == 2:
    if jogador == 0:
        print('\033[34mVOCÊ GANHOU\033[m')
    elif jogador == 1:
        print('\033[31mVOCÊ PERDEU\033[m')
    elif jogador == 2:
        print('\033[33mEMPATE\033[m')
    else:
        print('\033[31mJogada inválida\033[m')
print('O computador escolheu \033[33m{}\033[m.'.format(itens[computador]))
print('O jogador escolheu \033[33m{}\033[m.'.format(itens[jogador]))
print('\033[33m-=\033[m' * 20)