#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Digite o número que deseja ver a tabuada (Use número negativo para parar): '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} X {c:^2} = {c*num}')
print('TABUADA ENCERRADA')