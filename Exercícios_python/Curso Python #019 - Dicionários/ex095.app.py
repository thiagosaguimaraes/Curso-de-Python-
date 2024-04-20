jogador = {}
jogadores = []
partidas = []
tot = 0
while True:
    jogador['Jogador'] = input('Nome do jogador: ')
    part = int(input(f'Quantas partidas {jogador["Jogador"]} jogou? '))
    for g in range(1, part+1):
        partidas.append(int(input(f'Quantos gouls na {g}° partida? ')))
        tot +=
