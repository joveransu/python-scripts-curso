# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import requests

try:
    conexao = requests.get('http://www.pudim.com.br/')
    if conexao.status_code == 200:
        print('Site Pudim conectado.')
    else:
        print('Erro ao conectar com Pudim')
except:
    print('Erro ao conectar com Pudim')