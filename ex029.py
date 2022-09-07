#Escreva um programa que leia a velocidade de um carro, se ele ultrapassar 80Km/h mostrea uma mensagem dizendo que ele foi multado, a multa vai custar 7.00 por cada Km acima do limite

velo = float(input('Quantos kilomentros você está andando? '))
if velo > 80:
    print('Você foi multado em R$ {}'.format((velo-80)*7))