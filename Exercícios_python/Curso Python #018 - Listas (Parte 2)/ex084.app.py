dado = []
lista = []
cont = 1
maior = menor = 0
while True:
    print(f'{"=-" * 30} {cont}° paciente {"=-" * 30}')
    dado.append(input('Nome: ').strip().capitalize())
    dado.append(int(input('Peso: ')))
    cont += 1
    lista.append(dado[:])
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if menor > dado[1]:
            menor = dado[1]
        if maior < dado[1]:
            maior = dado[1]
    dado.clear()
    while True:
        soun = input('Quer continuar? [S/N] ').upper().strip()[0]
        if soun in 'SN':
            break

    if soun == 'N':
        break
print("=-" * 30)
print(lista)
print(f'Foram cadastrados {cont} pacientes')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in lista:
    if p[1] >= maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
print("=-" * 30)
