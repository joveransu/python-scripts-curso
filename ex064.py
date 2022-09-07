#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

contador = soma = pausar = 0
while pausar != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma += n
        contador += 1
    else:
        pausar = 999

print('Foram digitados {} números e a soma de todos é {}'.format(contador, soma))