# Faça um algoritmo que leia um preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Preço do produto: '))
desconto = float(input('Desconto do produto: '))
print('Preço atual do produto é R$: {:.2f}\nAplicando {}% de desconto, custará R$: {:.2f}.'.format(preco,desconto,(preco-(desconto/100)*preco)))
