#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numlist = list()
while True:
    num = int(input('Digite um número: '))
    if num in numlist:
        print('Número não adicionado, já existe na lista.')
    else:
        print(f'O número {num} foi adicionado.')
        numlist.append(num)

    res = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while not res in 'SN':
        res = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

    if res == 'N':
        break

numlist.sort()
print(f'Os valores digitados em ordem crescente é: {numlist}')
