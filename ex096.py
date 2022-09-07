# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    result = larg * comp
    print(f'A área de {larg}cm X {comp}cm é {result}m²')

larg = float(input('Qual a largura? '))
comp = float(input('Qual o comprimento? '))
area(larg, comp)