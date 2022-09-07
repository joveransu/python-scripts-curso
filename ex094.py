# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

pessoas = list()
mulheres = list()
velhos = list()
totalanos = 0

while True:
    pessoa = dict()
    pessoa['nome'] = input('Nome? ')
    pessoa['sexo'] = input(f"Sexo de {pessoa['nome']}[F/M]? ").upper()
    while not pessoa['sexo'] in 'MF':
        print('ERRO: Use M ou F')
        pessoa['sexo'] = input(f"Sexo de {pessoa['nome']}? ").upper()

    pessoa['anos'] = int(input(f"Idade de {pessoa['nome']}? "))

    totalanos += pessoa['anos']

    if pessoa['sexo'] in 'Ff':
            mulheres.append(pessoa['nome'])

    pessoas.append(pessoa.copy())
    pessoa.clear()


    res = input('Quer continuar? [S/N] ').strip().upper()[0]
    while not res in 'SN':
        print('ERRO: Use S ou N')
        res = input('Quer continuar [S/N]? ').strip().upper()[0]

    if res == "N":
        break

media = totalanos/len(pessoas)
for dados in pessoas:
    if dados['anos'] > media:
        velhos.append(dados)

print('-=' * 30)
print(f'Fora cadastradas {len(pessoas)} pessoas.')
print(f'A média de idade é {media}.')
print(f'As mulheres são: {mulheres}')
print(f'Pessoas acima da média são: {velhos}')
