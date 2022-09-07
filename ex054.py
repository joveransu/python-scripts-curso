#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
anoatual = date.today().year
maiores = 0
for c in range(0, 7):
    ano = int(input('Qual ano você nasceu? '))
    if anoatual - ano >= 18:
        maiores += 1

print('Existem {} pessoas maiores de idade.'.format(maiores))
print('Existem {} pessoas menores de idade.'.format(7-maiores))