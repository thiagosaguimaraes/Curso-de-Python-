print('=' * 50)
print(f'BRASILEIRÃO'.center(50))
print('=' * 50)
brasileirão = ('Palmeiras', 'Santos', 'Vasco da Gama', 'Grêmio', 'Flamengo', 'Corinthians', 'Internacional', 'Cruzeiro', 'São Paulo',
               'Atlético Mineiro', 'Botafogo', 'Fluminense', 'Coritiba', 'Bahia', 'Goiás', 'Guarani', 'Sport', 'Portuguesa', 'Atlético Paranaense', 'Vitória')
cont = 1
print('Lista de times do brasileirão')
for b in brasileirão:
    print(f'{cont:2}° lugar: {b}')
    cont += 1
print('-' * 50)
print(f'Os primeiros 5 colocados são: {brasileirão[:5]}')
print('-' * 50)
print(f'Os últimos 4 colocados são: {brasileirão[-4:]}')
print('-' * 50)
print(f'Times em ordem alfabético: {sorted(brasileirão)}')
print(f'O Chapecoense não tá em nenhuma posição')
print(f'O Baia está na {brasileirão.index("Bahia")+1}° colocação')
