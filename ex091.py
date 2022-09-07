# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from operator import itemgetter
from random import randint
from time import sleep


players = dict()
helped = dict()
for c in range(0, 4):
    helped[f'player{c}'] = randint(1, 6)
    print(f'Player {c+1} tirou {helped[f"player{c}"]}')
    sleep(1.5)

players = sorted(helped.items(), key=itemgetter(1), reverse=True)

print('-=' * 10, 'RANKING', '-=' * 10)
for i, v in enumerate(players):
    print(f'{i+1}° Lugar: {v[0]} teve {v[1]}')
    sleep(0.5)
print('-=' * 30)