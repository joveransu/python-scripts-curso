# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual seu salário? '))
aumentado = salario + (15/100*salario)
print('='*25)
print('O seu salário atual é de R$: {:.2f}\nCom aumento de 15% ficará R$: {:.2f}'.format(salario,aumentado))
print('='*25)
