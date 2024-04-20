'''matriz = []
valor = []
pos1 = 0
pos2 = 0
cont = 0
for n in range(1,10):
    valor.append(int(input(f'Digite um número para a posição [{pos1}, {pos2}]: ')))
    pos2 += 1
    matriz.append(valor[:])
    valor.clear()
    if n == 3:
        pos1 = 1
        pos2 = 0
    elif n == 6:
        pos1 = 2
        pos2 = 0
print('=-' * 30)
print(matriz)
for n in matriz:
    print(f'{n:^5}',end='')
    cont += 1
    if cont == 3 or cont == 6:
        print()
print()
print('=-' * 30)'''

# A do professor ae, fiquei felizão quando consegui fazer o meu sozinho,
# mas ai eu vi que o meu tava o dobro e linhas da solução do prof
# e eu percebi que nem tinha usado lista compostaKKKKKK
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
totpar = tot3 = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[ l ][ c ] % 2 == 0:
            totpar += matriz[ l ][ c ]
        if c == 2:
            tot3 += matriz[ l ][ c ]

    print()
print(f'A soma de todos os valores pares é {totpar}')
print(f'A soma dos valores da 3° coluna é {tot3}')
print(f'O maior valor da 2° linha é {max(matriz[1])}')
print()
