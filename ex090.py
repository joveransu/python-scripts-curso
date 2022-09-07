#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['nome'] = str(input('Digite um nome: ')).strip()
aluno['media'] = float(input('Qual sua media? '))
print(f"O aluno(a) {aluno['nome']} teve a média de {aluno['media']}.")
if aluno['media'] >= 7.0:
    aluno['situacao'] = 'Aprovado'
elif 5.5 <= aluno['media']:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print(f'Aluno foi {aluno["situacao"]}.')