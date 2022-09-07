#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: -1 Para binário -2 para octal -3 para hexadecimal
'''
print('\033[33m-=\033[m'*20)
n = int(input('Digite um número: '))
forma = int(input('Digite a conversão que deseja: (1 Para binário, 2 Para octal, 3 para hexadecimal)'))
binario = ''
if forma <= 1:
    if n > 1:
        b1 = n % 2
        n = n // 2
        binario = str(b1) + str(binario)
        if n > 0:
            b1 = n % 2
            n = n // 2
            binario = str(b1) + str(binario)
            if n > 0:
                b1 = n % 2
                n = n // 2
                binario = str(b1) + str(binario)
                if n > 0:
                    b1 = n % 2
                    n = n // 2
                    binario = str(b1) + str(binario)
                    if n > 0:
                        b1 = n % 2
                        n = n // 2
                        binario = str(b1) + str(binario)
    elif n == 1:
        binario = '1'
    else:
        binario = '0'
elif forma == 2:
    if n > 7:
        b1 = n % 8
        n = n // 8
        binario = str(b1) + str(binario)
        if n > 7:
            b1 = n % 8
            n = n // 8
            binario = str(b1) + str(binario)
            if n > 7:
                b1 = n % 8
                n = n // 8
                binario = str(b1) + str(binario)
                if n > 7:
                    b1 = n % 8
                    n = n // 8
                    binario = str(b1) + str(binario)
                    if n > 7:
                        b1 = n % 8
                        n = n // 8
                        binario = str(b1) + str(binario)
                    else:
                        binario = str(n) + str(binario)
                else:
                    binario = str(n) + str(binario)
            else:
                binario = str(n) + str(binario)
        else:
            binario = str(n) + str(binario)
    else:
        binario = n 
else:
    if n > 15:
        b1 = n % 16
        n = n // 16
        binario = str(b1) + str(binario)
        if n > 15:
            b1 = n % 16
            n = n // 16
            binario = str(b1) + str(binario)
            if n > 15:
                b1 = n % 16
                n = n // 16
                binario = str(b1) + str(binario)
                if n > 15:
                    b1 = n % 16
                    n = n // 16
                    binario = str(b1) + str(binario)
                    if n > 15:
                        b1 = n % 16
                        n = n // 16
                        binario = str(b1) + str(binario)
    else:
        binario = n 
print('\033[33m-=\033[m'*20)
if forma <= 1:
    print('Binário: {}'.format(binario))
elif forma == 2:
    print('Octal: {}'.format(binario))
else:
    print('hexadecimal: {}'.format(binario))
'''

n = int(input('Digite um número inteiro: '))
print('''Escolha uma conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
forma = int(input('Sua opção:  '))
if forma == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(n, bin(n)[2:]))
elif forma == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(n, oct(n)[2:]))
elif forma == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(n, hex(n)[2:]))
else:
    print('Opção de converção foi inválida.')

#print('{} convertido para HEXADECIMAL é igual a {}.'.format(n, hex(n)[2:]))
# .format(n, hex(n)[2:] o [2:] é para cortar o começo da string e ir até o final