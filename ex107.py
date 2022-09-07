from modulos import numeros

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {numeros.metade(p)}')
print(f'O dobro de {p} é {numeros.dobro(p)}')
print(f'Aumentando 10%, temos {numeros.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {numeros.diminuir(p, 13)}')