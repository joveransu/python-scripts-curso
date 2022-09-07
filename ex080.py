#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.


numlist = list()
for l in range(0,5):
    num = int(input('Digite um número: '))
    if len(numlist) == 0 or num > numlist[-1]:
        numlist.append(num)
        print(f'Inserido no fim')
    else:
        for c, v in enumerate(numlist):
            if num <= v:
                numlist.insert(c, num)
                print(f'Inserido na posição: {c}')
                break

print(f'Os valores digitados foram: {numlist}')
