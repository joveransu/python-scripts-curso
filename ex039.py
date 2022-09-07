#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade: - Se ele ainda vai se alistar ao serviço militar, - Se é a hora de se alistar, - Se já passou do tempo do alistamento, seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('\033[33m-=\033[m'*20)
ano = int(input('Diga o ano que você nasceu: '))

anoatual = date.today().year
idade = anoatual - ano

if idade < 18:
    print('Você irá se alistar em {} anos,'.format(18 - idade), end = ' ')
    print('você se alistará em {}'.format(ano + 18))
elif idade == 18:
    print('Você irá se alistar agora, CORRA!')
else:
    print('Você já se alistou a {} anos atrás,'.format(idade - 18), end = ' ')
    print('seu alistamento foi em {}'.format(ano + 18))