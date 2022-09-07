#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.]

vCasa = float(input('Qual valor da casa? '))
sala = float(input('Qual seu salário? '))
anos = int(input('Em quantos anos deseja pagar o emprestimo? '))

prestacao = vCasa / (anos * 12)
salP = 30 / 100 * sala

if prestacao > salP:
    print('\033[31mSeu salário não é suficiente para prestação desse imovel', end = ' ')
    print('Valor da prestação: {:.2f}'.format(prestacao), end = ' ')
    print('Porcetagem de 30%: {:.2f}!\033[m'.format(salP))
else:
    print('\033[32mSeu salário é suficiente para prestação desse imovel!', end = ' ')
    print('Valor da prestação: {:.2f}'.format(prestacao), end = ' ')
    print('Porcetagem de 30%: {:.2f}!\033[m'.format(salP))

