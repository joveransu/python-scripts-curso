def leiaInt(txt):
    while True:
        inteiro = input(f'{txt}').strip()
        try:
            inteiro = int(inteiro)
            break
        except Exception as erro:
            print(f'\033[31mERRO: Tipo "{erro}", número digitado não é válido.\033[m')
            continue

    return inteiro


def leiaFloat(txt):
    while True:
        decimal = input(f'{txt}').strip()
        try:
            decimal = float(decimal)
            break
        except Exception as erro:
            print(f'\033[31mERRO: Tipo "{erro}", número digitado não é válido.\033[m')
            continue

    return decimal