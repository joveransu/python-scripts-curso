# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print( 'Analise de uma PA')
termo = int(input('Digite um termo: '))
razão = int(input('Digite a razão: '))
cont = 0
maxPA = 10
while cont < maxPA:
    print('{} ->'.format(termo),end='')
    termo += razão
    cont += 1
    if cont == maxPA:
        print('PAUSA')
        v = int(input('Deseja mostrar mais quantos termos? [0 para sair]'))
        maxPA += v

print('Fim da PA, tivemos {} termos nela.'.format(cont))