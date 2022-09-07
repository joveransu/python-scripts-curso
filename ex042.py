#Refaça  o desafio 35 dos triangulos acrescentando o recurso de mostrar que tipo de triando será formado: Equilátero - Todos lados iguais, Isósceles - Dois lados iguais, Escaleno - Todos os lados diferentes

print('\033[33m-=\033[m' * 20)
print('Analisador de triângulos')
print('\033[33m-=\033[m' * 20)

a = float(input('Digite um numero: '))
b = float(input('Digite um numero: '))
c = float(input('Digite um numero: '))

if a < b + c and b < a + c and c < a + b:
    print('\033[32mTriângulo VERDADEIRO\033[m')
    if a == b == c:
        print('Triângulo Equilátero.')
    elif a == b or b == c or a == c:
        print('Triângulo Isósceles.')
    else:
        print('Triângulo Escaleno.')
else:
    print('\033[31mTriângulo FALSO\033[m')
print('\033[33m-=\033[m' * 20)
