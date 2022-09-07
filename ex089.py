#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = list()
data = list()

while True:
    data.append(str(input('Qual nome? ')).strip())
    data.append(float(input('Nota 1: ')))
    data.append(float(input('Nota 2: ')))
    alunos.append(data[:])
    data.clear()
    res = str(input('Quer continuar? '))
    if res in 'Nn':
        break

print('-=' * 25)
for index, valor in enumerate(alunos):
    print(f'ID: {index:^3} | Nome: {valor[0]:^15} | Média: {(valor[1]+valor[2])/2:.2f}')
print('-=' * 25)

while True:
    id_ = int(input('Digite um ID para ver analises [999 Para sair]: '))
    if id_ == 999 or id_ > len(alunos) - 1:
        break
    print(f'ID: {id_:^3} | Nome: {alunos[id_][0]:^15} | Notas: [{alunos[id_][1]:.2f}, {alunos[id_][2]:.2f}]')