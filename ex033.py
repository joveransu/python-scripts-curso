#Faça um programa que leia 3 numeros e mostre qual é o maior e qual o menor

n1 = int(input('Diga um numero: '))
n2 = int(input('Diga um numero: '))
n3 = int(input('Diga um numero: '))

#Forma 1
if n1 > n2 and n1 > n3 and n2 > n3:
    print('{} maior de todos e {} é o menor'.format(n1,n3))
if n1 > n2 and n1 > n3 and n2 < n3:
    print('{} maior de todos e {} é o menor'.format(n1,n2))
if n2 > n1 and n2 > n3 and n1 > n3:
    print('{} maior de todos e {} é o menor'.format(n2,n3))
if n2 > n1 and n2 > n3 and n1 < n3:
    print('{} maior de todos e {} é o menor'.format(n2,n1))
if n3 > n1 and  n3 > n2 and n1 > n2:
    print('{} maior de todos e {} é o menor'.format(n3,n2))
if n3 > n1 and  n3 > n2 and n1 < n2:
    print('{} maior de todos e {} é o menor'.format(n3,n1))

#Forma 2
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('{} maior de todos e {} é o menor'.format(maior,menor))
