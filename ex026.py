#Crie um programa que leia uma frase e mostre quantas vezes aparece a letra 'A', em que posição ela aparece a primeira vez, em que posição ela aparece a ultima vez.

frase = input('Digite uma frase: ').strip().upper()
print('Apareceu a letra A, {} vezes\nEla apareceu na posição {} na primeira vez\nEla apareceu na posição {} pela ultima vez.'.format(frase.count('A'),frase.find('A')+1,frase.rfind('A')+1))