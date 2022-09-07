#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão aritmetica.

termo = int(input('Digite um termo: '))
razão = int(input('Digite uma razão: '))

for c in range(termo, razão*10, razão):
    if c < razão*11:
        print(c)