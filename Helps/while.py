from pickle import TRUE


n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('Fim')

soma = 0
while True:
    n = int(input('Digite um número [Digite 0 para parar]: '))
    if n == 0:
        break
    soma += n
print(f'Fim, a soma dos números foram {soma}.')