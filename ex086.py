#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[],[],[]]

for c in range(0,3):
    for v in range(0, 3):
        matriz[c].append(int(input(f'Digite um número para [{c},{v}]: ')))

for c in range(0,3):
    print(matriz[c])