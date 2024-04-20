lista = []
num = 1
maior = menor = meio = 0
for cont in range(1, 6):
    n = int(input(f'Digite o {cont}° valor: '))
    if cont == 1 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionando na posição {pos} da lista...')
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados em ordem são: {lista}')
        
    