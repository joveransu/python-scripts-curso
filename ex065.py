#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

res = 'S'
maior = cont = menor = soma = 0
print('-=' * 20)
while res != 'N':
    adicional = int(input('Digite um número: '))
    soma += adicional
    if cont == 0:
        menor = maior = adicional
    else:
        if adicional < menor:
            menor = adicional
        if adicional > maior:
            maior = adicional
    cont += 1
    res = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if res != 'N':
        res = 'S'
print('-=' * 20)
print('Foram digitados {} valores.\nA média é {}\nO menor valor é {}\nO maior número é {}'.format(cont,soma/cont,menor,maior))
    