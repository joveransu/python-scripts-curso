'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

maioridade = homens = mulheres = 0
while True:
    idade = int(input('Qual idade? '))
    sexo = ' '
    while not sexo in 'MF':
        sexo = str(input('Qual sexo? [M/F]')).strip().upper()[0]
    
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1

    res = ' '
    while not res in 'NS':
        res = str(input('Pessoa cadastrada, quer continuar? [S/N]')).strip().upper()[0]
    if res == 'N':
        break
print(f'Cadastros encerrados\nTivemos {maioridade} pessoas maiores de idade\nForam {homens} homens cadastrados\nE {mulheres} mulheres tem menos de 20 anos.')
        