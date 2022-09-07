#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('-=' * 16)
produtos = ('Maçã', 0.95, 'Goiaba', 0.63, 'Manga', 2.35, 'Melancia', 4.75)
print('{:.<25}{:.>7}'.format('Produtos', 'Preços'))
print('-=' * 16)
#for c in range(0, len(produtos), 2):
#    print('{:.<25}{:.>7}'.format(produtos[c], 'R$ ' + str(produtos[c+1])))

for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<25}', end=' ')
    else:
        print(f'R$ {produtos[c]:>4.2f}')