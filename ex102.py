# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
        -> Ele vai calcular um fatorial de um número.
        parm: num -> O numero que deseja o fatorial
        parm: show -> True para mostrar os calculos
        return valor do fatorial do numero
    """
    from time import sleep
    if num < 0:
        num = 0
    c = num
    valor = 1
    if show:
        print(f'Calculando o fatorial de {num}...', flush=True)
    sleep(0.3)
    while c != 0:
        valor *= c
        if show:
            print(f'{valor} ->', end=' ', flush=True)
        sleep(0.5)
        c -= 1
    if show:
        print(f'\nO fatorial de {num} é {valor}')
    return valor


print(fatorial(5, True))

help(fatorial)