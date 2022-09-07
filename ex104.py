# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(txt):

    while True:
        msg = input(txt)
        if msg.isnumeric():
            break
        else:
            print('\033[31mPor favor, digite um número.\033[m')
    return msg


n = leiaInt('Digite um numero: ')
print(f'Você digitou o numero {n}')