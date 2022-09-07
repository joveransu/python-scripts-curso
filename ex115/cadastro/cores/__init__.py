cores = {
    'Preto':30,
    'Vermelho':31,
    'Verde':32,
    'Amarelo':33,
    'Azul':34,
    'Magenta':35,
    'Cyan':36,

    'FPreto':40,
    'FVermelho':41,
    'FVerde':42,
    'FAmarelo':43,
    'FAzul':44,
    'FMagenta':45,
    'FCyan':46
}

def get_color(fonte='default', fundo='default'):
    """
        -> Retorna uma cor para terminal
        - fonte = cor da fonte que deseja.
        - fundo = cor do fundo que deseja.

        NOTE: Usar a função sem parâmetros irá resetar as cores.

        CORES: Preto, Vermelho, Verde, Amarelo, Azul, Magenta, Cyan

        ESPECIAL FONTES: Branco, Negrito, Inverte, Remover
    """

    if fundo == 'default' and fonte == 'default':
        retorno = '\033[0;0m'
    else:
        fundo = 'F' + fundo
        if fonte == 'Negrito':
            retorno = '\033[;1m'

        elif fonte == 'Inverte':
            retorno = '\033[;7m'

        elif fonte == 'Branco':
            retorno = '\033[1;97m'
        
        elif fundo == 'FBranco':
            retorno = '\033[1;107m'

        else:
            if fonte != 'default' and fundo != 'Fdefault':
                retorno = f"\033[{cores[fonte]};{cores[fundo]}m"

            elif fonte != 'default' and fundo == 'Fdefault':
                retorno = f"\033[{cores[fonte]}m"

            elif fonte == 'default' and fundo != 'Fdefault':
                retorno = f"\033[{cores[fundo]}m"
                
    return retorno