#Tuplas = As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

def Linha():
    print('\033[34m-=\033[m' * 20)
lanches = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanches)
print(lanches[2])
print(lanches[-3])
print(lanches[:2])
Linha()
for pos, comida in enumerate(lanches):
    print(f'O {pos+1}° é {comida}.')

Linha()
a = (1, 2, 3)
b = (4, 5, 6, 7)
c = a + b
print(c)
Linha()
c = b + a
print(c)

#Deletar uma tupla
#del(a)
#print(a)

print('-=' * 18)
produtos = ('Maçã', 0.95, 'Goiaba', 0.63, 'Manga', 2.35, 'Melancia', 4.75)
print('{:.<25}{:.>7}'.format('Produtos', 'Preços'))
print('-=' * 18)

for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<25}', end=' ')
    else:
        print(f'R$ {produtos[c]:>4.2f}')