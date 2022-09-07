#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.


numlist = [[], []]
for c in range(0,7):
    num = int(input(f'Digite o {c+1}° valor: '))
    if num % 2 == 0:
        numlist[0].append(num)
    else:
        numlist[1].append(num)

numlist[1].sort()
numlist[0].sort()

print(f'Valores pares {numlist[0]}')
print(f'Valores pares {numlist[1]}')