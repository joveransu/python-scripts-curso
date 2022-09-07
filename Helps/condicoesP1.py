tempo = int(input('Quantos anos o carro tem? '))
#print('Carro novo' if tempo <= 3 else 'Carro velho')

if tempo < 3:
    print('Carro Novo')
elif tempo == 3:
    print('Carro Normal')
else:
    print('Carro velho')
