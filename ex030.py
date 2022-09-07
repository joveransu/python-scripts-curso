#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

num = int(input('Diga um número: '))
if num % 2 == 1:
    print('O número {} é IMPAR.'.format(num))
else:
    print('O número {} é PAR.'.format(num))