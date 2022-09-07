'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

'''
dinheiro = int(input('Qual valor você deseja sacar? '))
nota50 = nota20 = nota10 = nota1 = 0
while True:
    if dinheiro >= 50:
        dinheiro -= 50
        nota50 += 1
    elif dinheiro >= 20:
        dinheiro -= 20
        nota20 += 1
    elif dinheiro >= 10:
        dinheiro -= 10
        nota10 += 1
    elif dinheiro >= 1:
        dinheiro -= 1
        nota1 += 1
    elif dinheiro <= 0:
        break
print(f'Você recebeu {nota50} cédulas de R$ 50.00')
print(f'Você recebeu {nota20} cédulas de R$ 20.00')
print(f'Você recebeu {nota10} cédulas de R$ 10.00')
print(f'Você recebeu {nota1} cédulas de R$ 1.00')
'''

dinheiro = int(input('Qual valor você deseja sacar? '))
nota50 = nota20 = nota10 = nota1 = 0

while True:
    if dinheiro >= 50:
        nota50 = dinheiro // 50
        dinheiro %= 50
        print(f'Você recebeu {nota50} cédulas de R$ 50.00')
    if dinheiro >= 20:
        nota20 = dinheiro // 20
        dinheiro %= 20
        print(f'Você recebeu {nota20} cédulas de R$ 20.00')
    if dinheiro >= 10:
        nota10 = dinheiro // 10
        dinheiro %= 10
        print(f'Você recebeu {nota10} cédulas de R$ 10.00')
    if dinheiro >= 1:
        nota1 = dinheiro // 1
        dinheiro %= 1
        print(f'Você recebeu {nota1} cédulas de R$ 1.00')
    if dinheiro == 0:
        break

'''
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
'''