# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador, gols):
    if len(jogador) == 0:
        jogador = '<Desconhecido>'
    if len(gols) == 0 or gols.isnumeric() == False:
        gols = 0
    print(f'O jogador {jogador} fez {gols} gol(s).')

ficha(input('Qual nome do jogador? '), input('Quantos gols? '))
