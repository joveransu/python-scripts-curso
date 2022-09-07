#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmr = 0.15
diaria = 60

dias = int(input('Quantos dias foram utilizado? '))
km = float(input('Quantos kilometros foram rodados? '))

valor = (dias * diaria) + (km * kmr)

print('='*25)
print('Foram utilizados {} dias.\nFoi pecorrido {:.2f}Km.\nValor a ser pago R$: {:.2f}'.format(dias,km,valor))
print('='*25)
