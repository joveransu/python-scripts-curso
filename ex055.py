#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = (0,0)
menor = (0,10000**200)
for c in range(1,6):
    n = float(input('Qual o peso da pessoa? '))
    if n > maior[1]:
        maior = (c, n)
    if n < menor[1]:
        menor = (c, n)
print('A pessoa mais pesada foi a {}° com {:.2f} Kg.'.format(maior[0], maior[1]))
print('A pessoa menos pesada foi a {}° com {:.2f} Kg.'.format(menor[0], menor[1]))

#Sem tuplas e gambiarra

maior = 0
menor = 0
for p in range(0, 5):
    peso =  float(input('Qual o peso da pessoa? '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('A pessoa mais pesada tem {:.2f} Kg.'.format(maior))
print('A pessoa menos pesada tem {:.2f} Kg.'.format(menor))