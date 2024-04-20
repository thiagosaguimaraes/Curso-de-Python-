lista = ('Pão', 2.00,
         'Biscoito', 4.00,
         'Batata', 3.00,
         'Nescau', 8.00)
cont = 1
tracin = '=' * 50
print(tracin.center(50))
print('Lista de preços'.center(50))
print(tracin.center(50))
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
tracin = '=' * 50
