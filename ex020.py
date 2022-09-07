#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a sorteada

import random

al1 = input('Digite o nome do primeiro aluno: ')
al2 = input('Digite o nome do segundo aluno: ')
al3 = input('Digite o nome do terceiro aluno: ')
al4 = input('Digite o nome do quarto aluno: ')

lista = [al1, al2, al3, al4] #Tabelas no Python são colchetes
random.shuffle(lista)
print('Ordem de apresentação {}.'.format(lista))

# Aqui eu irei embaralhar de uma maneira menos bagunçadas
#escolhido = random.sample(lista, 4) 
#print('Ordem de apresentação {}.'.format(escolhido))
