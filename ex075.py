'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''

valores = (int(input('Digite um número: ')), int(input('Digite mais um número: ')), int(input('Digite outro número: ')), int(input('Digite o último número: ')))

print(f'Foram encontrados {valores.count(9)} números 9')

if 3 in valores:
    print(f'O numero 3 foi encontrado na posição {valores.index(3)+1}° pela primeira vez.')
else:
    print('Tupla não possui numero 3.')

cont = 0
for n in valores:
    if n % 2 == 0:
        cont += 1
        print(f'Numero {n} é par')

if cont == 0:
    print('Não tivemos numeros pares')