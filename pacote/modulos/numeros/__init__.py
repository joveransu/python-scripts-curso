def moeda(n=0, moeda='R$'):
    """
        -> Transforma o valor em um número monetário.
        - N = Valor a ser tranformado.
        return = string com os valor como monetário (R$ 2377,00)
    """
    valor = f'{moeda} {n:.2f}'
    formated = valor.replace('.', ',')
    return formated


def aumentar(n=0, p=0, formated=False):
    """
        -> Aumenta o preço conforme a porcentagem.
        - N = Preço que irá ser aumentado.
        - P = Porcentagem de aumento.
        - formated = Default False, se o numero virá formatado em real
        return = O valor com a porcentagem de aumento.
    """
    
    aum = p/100 * n
    if formated:
        return moeda(n + aum)
    return n + aum


def diminuir(n=0, p=0, formated=False):
    """
        -> Diminui o preço conforme a porcentagem.
        - N = Preço que irá ser redução.
        - P = Porcentagem de redução.
        - formated = Default False, se o numero virá formatado em real
        return = O valor com a porcentagem de redução.
    """
    
    dim = p/100 * n

    if formated:
        return moeda(n - dim)
    return n - dim


def dobro(n=0, formated=False):
    """
        -> Dobra o valor desejado
        - N = Valor que será dobrado.
        - formated = Default False, se o numero virá formatado em real
        return = O valor dobrado 
    """

    if formated:
        return moeda(n * 2)
    return n * 2


def metade(n=0, formated=False):
    """
        -> Divide por 2 o valor desejado
        - N = Valor que será dividido por 2.
        - formated = Default False, se o numero virá formatado em real
        return = O valor dividido 
    """

    if formated:
        return moeda(n / 2)
    return n / 2

def resumo(num, aum, red):
    print('=' * 25)
    print('RESUMO DO VALOR'.center(25))
    print('=' * 25)

    print(f'{"ANALIZANDO:":<13} {moeda(num):<10}')
    print(f'{"METADE:":<13} {metade(num, True):<10}')
    print(f'{"DOBRO:":<13} {dobro(num, True):<10}')
    print(f'{f"AUMENTO {aum}%:":<13} {aumentar(num, aum, True):<10}')
    print(f'{f"REDUÇÃO {red}%:":<13} {diminuir(num, red, True):<10}')

    print('=' * 25)