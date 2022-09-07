#Faça um programa que leia o nome de uma pessoa e mostre o primeiro e ultimo nome dela separadamente.

nome = str(input('Digite seu nome: ')).strip()
print('Primeiro nome: {}\nUltimo nome: {}'.format(nome[:nome.find(' ')], nome[nome.rfind(' ')+1:]))

nome = nome.split()
print('Primeiro nome: {}\nUltimo nome: {}'.format(nome[0], nome[len(nome)-1]))