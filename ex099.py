# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(* num):
    mai = c = 0
    print(f'Analisando numero')
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if c == 0:
            mai = valor
        else:
            if valor > mai:
                mai = valor
        c += 1
    print('FIM')
    print(f'Foram ditos {c} números e o maior valor é {mai}.')


maior(5, 9, 1, 4, 6)