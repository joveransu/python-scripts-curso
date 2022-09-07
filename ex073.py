'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
'''

brasileirao = ('Palmeiras', 'Athletico-PR', 'Atlético-MG','Fluminense','Corinthians','Internacional','Bragantino','Flamengo','São Paulo','Ceará','Santos','Goiás','Botafogo','Avaí','Cuiabá','Coritiba','América-MG','Atlético-GO','Fortaleza','Juventude')

print(f'Os 5 primeiros são: {brasileirao[:5]}')
print(f'Os 4 ultimos são: {brasileirao[-4:]}')
print(f'Em ordem alfabética: {sorted(brasileirao)}')
print(f"O clube Cuiabá foi encontrado na {brasileirao.index('Cuiabá')+1}° posição")

#for pos, clube in enumerate(brasileirao):
#    if clube == 'Cuiabá':
#        print(f'O clube Cuiabá foi encontrado na {pos+1}° posição')
#        break