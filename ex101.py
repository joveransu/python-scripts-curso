# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano=2000):
    from datetime import datetime
    vototype = 'NEGADO'
    anoagora = datetime.now().year
    idade = anoagora - ano
    if 16 <= idade < 18 or idade >= 65:
        vototype = 'OPCIONAL'
    elif idade >= 18:
        vototype = 'OBRIGATORIO'
    return vototype, idade


vototype, idade = voto(int(input('Que ano você nasceu? ')))
print(f'Você tem {idade} e seu voto é {vototype}.')