# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
gols = []
jogador['nome'] = input('Nome: ').strip()
jogador['jogo'] = int(input('Jogos: '))
jogador['tota'] = 0

for c in range(0, jogador['jogo']):
    gol = int(input(f'Gols na partida{c}: '))
    gols.append(gol)
    jogador['tota'] += gol

jogador['gols'] = gols

print('-=' * 20)
print(jogador)

print('-=' * 20)
print(f"- Jogador: {jogador['nome']}")
print(f"- Gols: {gols}")
print(f"- Total de gols: {jogador['tota']}")

print('-=' * 20)
print(f"{jogador['nome']} jogou {jogador['jogo']} partidas.")
for c in range(0, jogador['jogo']):
    print(f"Na partida {c} fez {jogador['gols'][c]} gols.")
print(f"Teve um total de {jogador['tota']} golaços.")