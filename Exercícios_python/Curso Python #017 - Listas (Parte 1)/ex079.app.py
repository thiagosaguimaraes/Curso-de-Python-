lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a possição {c}: ')))
    if c == 1:
        maior = menor = lista[c]
    else:

        if lista[c] < menor:
            menor = lista[c]

        if lista[c] > maior:
            maior = lista[c]

print('=-' * 50)
print(f'Você digitou os valores: {lista}')
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for posição, valor in enumerate(lista):
    if valor == menor:
        print(f'{posição}...', end='')
print()

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for posição, valor in enumerate(lista):
    if valor == maior:
        print(f'{posição}...', end='')
print()
print('=-' * 50)
