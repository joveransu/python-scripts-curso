#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date

ano = int(input('Digite um ano: '))
#if ano % 4 == 0:
#    if ano % 100 == 0:
#        if ano % 400 == 0:
#            print('Ano bissexto')
#        else:
#            print('Ano não bissexto')
#    else:
#        print('Ano bissexto')
#else:
#    print('Ano não bissexto')
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano bissexto')
else:
    print('Ano não bissexto')