#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: - O primeiro valor é maior - o segundo valor é maior - não existe valor maior, os dois são iguais.
print('\033[33m-=\033[m'*20)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro numero: '))
print('\033[33m-=\033[m'*20)
if n1 > n2:
    print('Primeiro valor é maior.')
elif n2 > n1:
    print('Segundo valor é maior.')
else:
    print('Os Valores são iguais.')