#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: A media de idade do grupo - Qual o nome do homem mais velho - Quantas mulheres tem menos de 20 anos

media = 0
homemV = ''
idadeH = 0
quantm = 0

for c in range(0,4):
    nome = str(input('Qual seu nome? ')).strip()
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo? ')).upper().strip()
    media += idade
    if sexo in 'Mm':
        if idadeH < idade:
            homemV = nome
    else:
        if idade < 20:
            quantm += 1

print('A idade média do grupo é {:.2f}.'.format(media/4))
print('O nome do homem mais velho é {}.'.format(homemV))
print('Existe {} mulheres menor de 20 anos.'.format(quantm))
