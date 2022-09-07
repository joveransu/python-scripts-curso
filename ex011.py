# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = largura * altura
print('Altura = {}\nLargura = {}\nÁrea = {}m²\nTinta necessária = {}Lts'.format(altura,largura,area,(area/2)))
