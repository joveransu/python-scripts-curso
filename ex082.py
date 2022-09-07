#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numlist = list()
while True:
    numlist.append(int(input('Digite um número: ')))
    res = input('Quer continuar? ').strip()
    if res in 'Nn':
        break

parlist = list()
imparlist = list()

for v in numlist:
    if v % 2 == 0:
        parlist.append(v)
    else:
        imparlist.append(v)

print(f'Todos os números: {numlist}')
print(f'Números pares: {parlist}')
print(f'Números impares: {imparlist}')
