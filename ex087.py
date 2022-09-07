#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[],[],[]]
soma = 0
for c in range(0,3):
    for v in range(0, 3):
        matriz[c].append(int(input(f'Digite um número para [{c},{v}]: ')))

for c in range(0,3):
    print(matriz[c])
    for v in range(0,3):
        if matriz[c][v] % 2 == 0:
            soma += matriz[c][v]

print(f'A soma dos valores pares são {soma}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
matriz[1].sort()
print(f'O maior valor da segunda linha é {matriz[1][-1]}')