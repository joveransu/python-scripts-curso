#Crie um programa que leia duas notas do aluno e diga sua media se: - Media abaixo de 5, reprovado| - Media entre 5 e 6.9, recuperação | - Media maior que 7, Aprovado
print('\033[33m-=\033[m'*20)

n1 = float(input('Qual sua primeira nota? '))
n2 = float(input('Qual sua segunda nota? '))

media = (n1 + n2) / 2

if media < 5:
    print('\033[31mVocê foi... REPROVADO!\033[m')
elif 7 > media >= 5:
    print('\033[33mVocê foi... colocado em RECUPERAÇÃO!\033[m')
else:
    print('\033[32mVocê foi... APROVADO!\033[m')
print('Sua média final foi {:.2f}.'.format(media))
print('\033[33m-=\033[m'*20)