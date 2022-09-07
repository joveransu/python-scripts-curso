#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

nome = input('Diga um nome de pessoa: ').strip()
print('Tem Silva no nome? {}'.format(bool(nome.upper().find('SILVA')+1)))
print('Tem Silva no nome? {}'.format('SILVA' in nome.upper()))
