#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: - A vista 10% de desconto, - A vista cartão 5% de desconto, - Em até duas vezes no cartão preço normal, - 3x ou mais no cartão 20% de juros

print(' {:=^40} '.format(' LOJAS ANSU '))
valor = float(input('Qual valor do produto? '))
print('''Qual forma de pagamento?
[ 1 ] A vista dinheiro/cheque
[ 2 ] A vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
forma = int(input('Escolha? '))

if forma == 4:
    parcelas = int(input('Quantas parcelas? '))

parcelado = valor + (20/100 * valor)
print('\033[33m-=\033[m' * 20)
if forma <= 1:
    avista = valor - (10/100 * valor)
    print('Preço do produto R$: {:.2f}, Valor a vista será R$: {:.2f}.'.format(valor, avista))
elif forma == 2:
    avistaC = valor - (5/100 * valor)
    print('Preço do produto R$: {:.2f}, Valor a vista no cartão será R$: {:.2f}.'.format(valor, avistaC))
elif forma == 3:
    print('Preço do produto R$: {:.2f}, Valor em até duas vezes no cartão será R$: {:.2f}.'.format(valor, valor))
elif forma == 4:
    print('Preço do produto R$: {:.2f}, Valor em até três vezes no cartão será R$: {:.2f}. \nValor por mês {:.2f}'.format(valor, parcelado, parcelado/parcelas))
else:
    print('\033[31mOpção inválida de pagamento, tente novamente.\033[m')
print('\033[33m-=\033[m' * 20)
