#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: - Abaixo de 18.5 = Abaixo do peso, - Entre 18.5 e 25 = Peso Ideal, - 25 até 30 = Sobrepeso, - 30 até 40 Obsidade, - Acima de 40 = Obesidade mórbida

# IMC = kg / (m)²
print('\033[33m-=\033[m' * 20)
print('\033[35mCalcular IMC.\033[m')
peso = float(input('Qual seu peso? '))
altura = float(input('Quanto você mede? '))
print('\033[33m-=\033[m' * 20)

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é de {:.2f}, você está abaixo do peso.'.format(imc))
elif imc < 25:
    print('Seu IMC é de {:.2f}, você está com peso ideal.'.format(imc))
elif imc < 30:
    print('Seu IMC é de {:.2f}, você está com sobrepeso.'.format(imc))
elif imc < 40:
    print('Seu IMC é de {:.2f}, você está com obsidade.'.format(imc))
else:
    print('Seu IMC é de {:.2f}, você está com obsidade mórbida.'.format(imc))

print('\033[33m-=\033[m' * 20)

