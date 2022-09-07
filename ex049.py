# Refaça o desafio 009, mostrando a tabuada de um numero que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número: '))
print('\033[33m-=\033[m' * 20)
print('TABUDADA DO {}'.format(n))
print('\033[33m-=\033[m' * 20)
for c in range(1, 11):
    print('{} X {:2} = {}'.format(n, c, (n*c)))
print('\033[33m-=\033[m' * 20)
