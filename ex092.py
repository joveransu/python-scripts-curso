# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. 35 anos de contribuição


import datetime

pessoa = dict()
pessoa['nome'] = str(input('Qual seu nome? ')).strip()
pessoa['nasc'] = int(input('Qual ano você nasceu? '))
pessoa['ctps'] = int(input('Carteira de trabalho: '))

anoagora = datetime.datetime.now().year

pessoa['idade'] = anoagora - pessoa['nasc']

if pessoa['ctps'] == 0:
    print('-=' * 30)
    print(f"- Nome: {pessoa['nome']}")
    print(f"- Nascimento: {pessoa['nasc']}")
    print(f"- Idade: {pessoa['idade']}")
    print(f"- CTPS: {pessoa['ctps']}")
else:
    pessoa['cont'] = int(input('Que ano você foi contratado? '))
    pessoa['sala'] = int(input('Qual seu salário? '))
    pessoa['apos'] = pessoa['cont'] - anoagora + 35 + pessoa['idade']
    
    print('-=' * 30)
    print(f"- Nome: {pessoa['nome']}")
    print(f"- Nascimento: {pessoa['nasc']}")
    print(f"- Idade: {pessoa['idade']}")
    print(f"- CTPS: {pessoa['ctps']}")
    print(f"- Salário: {pessoa['sala']}")
    print(f"- Aposento: {pessoa['apos']}")

