jogador = {}
goles = []
total = 0
cont = 1
jogador['nome do jogador'] = input('Nome do jogador: ').strip().capitalize()
partidas = int(input(f'Quantas partidas {jogador["nome do jogador"]} jogou? '))
print('-' * 20)
for p in range(1, partidas+1):
    gous = int(input(f'Quantos gols na {p}° partida? '))
    goles.append(gous)
    total += gous

jogador['gols'] = goles
jogador['total de gols'] = total
print('=-' * 30)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('=-' * 30)
print(f'O jogador {jogador["nome do jogador"]} jogou {partidas} partidas')
for v in jogador['gols']:
    print(f'=> Na {cont}° partida fez {v} gols')
    cont += 1
print(f'Fez um total de {jogador["total de gols"]} de gols')
print('=-' * 30)
