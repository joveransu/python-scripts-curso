#Crie um programa que leia o nome completo de uma pessoa e mostre, nome com todas letras maiusculas, com todas letras minusculas, quantas letras tem sem considerar os espaços e e quantas letras tem o primeiro nome

nome = input('Digite seu nome: ').strip()
print(nome.upper())
print(nome.lower())
print('Existe {} carácteres removendo os espaços'.format(len(nome) - nome.find(' ')))
editado = nome.split()
print('O primeiro nome é {} e tem {} carácteres.'.format(editado[0],len(editado[0])))
