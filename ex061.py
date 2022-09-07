#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

print( 'Analise de uma PA')
termo = int(input('Digite um termo: '))
razão = int(input('Digite a razão: '))
cont = 1
while cont < 11:
    print('{} '.format(termo),end='')
    print('-> ' if cont != 0 else '', end='')
    termo += razão
    cont += 1
print('Fim da PA')