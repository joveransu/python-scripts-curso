#A confederção nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: - ate 9 anos Mirim, - Ate 14 anos Infantil, -Ate 19 Anos Junior, Ate 20 anos Sênior e Acima é Master

from datetime import date

nasc = int(input('Que ano você nasceu? '))
anoatual = date.today().year
idade = anoatual - nasc
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade <= 20:
    print('Sua categoria é SENIOR')
else:
    print('Sua categoria pe MASTER')