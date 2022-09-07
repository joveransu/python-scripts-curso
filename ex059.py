'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print('-=' * 20)
progra = 0
while progra != 5:
    progra = int(input('O que deseja fazer com esses números?\n[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa.'))
    print('-=' * 20)
    if progra == 1:
        print('A soma entre {} e {} é igual a {}'.format(num1, num2, num1+num2))
    elif progra == 2:
        print('A multiplicação entre {} e {} é igual a {}'.format(num1, num2, num1*num2))
    elif progra == 3:
        if num1 > num2:
            print('O número 1 ({}) é maior que o número 2 ({}).'.format(num1, num2))
        elif num2 > num1:
            print('O número 2 ({}) é maior que o número 1 ({}).'.format(num2, num1))
        else:
            print('Os números são iguais.')
    elif progra == 4:
        print('Escolha novos números.')
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
    elif progra > 5:
        print('Opção inválida, tente novamente.')
    print('-=' * 20)
print('Fim do programa.')