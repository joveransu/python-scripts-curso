#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

Sexo = str(input('Digite um sexo [M/F]: ')).strip().upper()[0]
while not Sexo in 'MF':
    Sexo = str(input('Dados inválidos, por favor, digite um sexo [M/F]: ')).upper().strip()[0]

if Sexo == 'M':
    print('Você digitou o sexo masculino.')
else:
    print('Você digitou o sexo Feminino.')

