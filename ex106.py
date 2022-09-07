# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

def txtorg(txt):
    tam = len(txt) + 4
    print(f'\033[47m~\033[m' * tam)
    print(f'  \033[47m{txt}\033[m')
    print(f'\033[47m~\033[m' * tam)


def ajudando(cmd):
    from time import sleep
    txtorg(f'Mostrando ajuda de {cmd}...')
    sleep(0.5)
    print(f'\033[47m{help(cmd)}\033[m', flush=True)




while True:
    cmd = input(f'\033[44mQual comando deseja usar? \033[m').strip()
    if cmd.upper() == 'FIM':
        break
    else:
        ajudando(cmd)