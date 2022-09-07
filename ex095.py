# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = list()
jogador = dict()
gols = list()

while True:
    jogador['nome'] = input('Nome: ').strip()
    jogador['jogo'] = int(input('Jogos: '))
    jogador['tota'] = 0

    for c in range(0, jogador['jogo']):
        gol = int(input(f'Gols na partida{c}: '))
        gols.append(gol)
        jogador['tota'] += gol

    jogador['gols'] = gols.copy()
    jogador['apro'] = jogador['tota']/jogador['jogo']*100

    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()

    res = input('Quer continuar [S/N]? ').strip()[0]
    if res in 'Nn':
        break

print(f'{"Code":<5}|{"Nome":<12}|{"Partidas":<9}|{"Aproveitamento":<16}|Gols')
print('-=' * 25)
for idx, dados in enumerate(jogadores):
    print(f"{idx:<5}|{dados['nome']:<12}|{dados['jogo']:<9}|{dados['apro']:<16.2f}|{dados['gols']}")
print('-=' * 25)

while True:
    id_list = int(input('Deseja informações extra de algum jogador? Diga o ID '))
    if id_list == 999:
        break
    if id_list < 0 or id_list > len(jogadores):
        id_list = int(input(f'ID Inválido, Diga o ID entre 0 e {len(jogadores)}, [999 para encerrar]'))
    else:
        print(f"{jogadores[id_list]['nome']} jogou {jogadores[id_list]['jogo']} partidas.")
        for c in range(0, jogadores[id_list]['jogo']):
            print(f"Na partida {c} fez {jogadores[id_list]['gols'][c]} gols.")
        print(f"Teve um total de {jogadores[id_list]['tota']} golaços.")
