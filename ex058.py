# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
pc = randint(0,10)
palpites = 1
print('Sou seu computador, pensei em um número de 0 a 10, será que você consegue adivinhar?')
player = int(input('Escolha um número de 0 a 10: '))
while pc != player:
    palpites += 1
    if pc < player:
        print('O valor é menor.')
    elif pc > player:
        print('O valor é maior.')
    player = int(input('Você errou. Escolha outro número de 0 a 10: '))
print('Você acertou, tentativas usadas {}, número escolhido {}.'.format(palpites, player))
