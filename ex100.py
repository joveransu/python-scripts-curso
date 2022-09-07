# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(0, 9))


def somaPar(num):
    tot = 0
    for c in num:
        if c % 2 == 0:
            tot += c

    print(f'Lista selecionada foi {num}.')
    print(f'A soma dos numeros pares dessa lista é {tot}')


numeros = list()
sorteia(numeros)
somaPar(numeros)