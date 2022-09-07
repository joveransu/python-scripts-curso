#Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento. Para salarios superiores a 1.250 calcule um aumento de 10% e para inferiores o aumento de 15%

sala = float(input('Digite seu salário: R$'))
if sala >= 1250.00:
    print('Seu novo salário é de R$ {:.2f}'.format(10/100*sala+sala))
else:
    print('Seu novo salário é de R$ {:.2f}'.format(15/100*sala+sala))