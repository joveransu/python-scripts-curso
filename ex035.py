#Desenvolva um programa que leia o comprimento de três restas e diga ao usuário se elas podem ou não formar um triangulo
# 
'''
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b

Exemplo:
Com os três segmentos de reta medindo 5cm, 10cm e 9cm, podemos formar um triângulo?
Vamos aplicar a regra da condição de existência de um triângulo para todos os lados.
|10 – 9| < 5 < 10 + 9
1 < 5 <19 (VERDADEIRO)

|9 – 5| < 10 < 9 + 5
4 < 10 < 14 (VERDADEIRO)

|5 – 10| < 9 < 10 + 5
5 < 9 < 15 (VERDADEIRO)

Quando um lado não obedece à regra não é possível existir um triângulo.

Cada um precisa ser menor que a soma dos outros dois lados
a < b + c
b < c + a
c < a + b
'''

print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)

a = float(input('Digite um numero: '))
b = float(input('Digite um numero: '))
c = float(input('Digite um numero: '))

cond1 = False
cond2 = False
cond3 = False

if (b - c) < a < b + c:
    cond1 = True
if (a - c) < b < a + c:
    cond2 = True
if (a - b) < c < a + b:
    cond3 = True

print('Triângulo VERDADEIRO' if cond1 and cond2 and cond3 else 'Triângulo FALSO')

if a < b + c and b < a + c and c < a + b:
    print('Triângulo VERDADEIRO')
else:
    print('Triângulo FALSO')