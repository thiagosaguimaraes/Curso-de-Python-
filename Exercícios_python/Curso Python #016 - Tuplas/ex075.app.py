valores = (int(input('Digite o 1° valor: ')), int(input('Digite o 2° valor: ')), int(
    input('Digite o 3° valor: ')), int(input('Digite o 4° valor: ')))
print('Os valores digitados foram: ')
for n in valores:
    print(f'{n}', end=' ')
print(f'\nO número 9 apareceu {valores.count(9)} vez(es)')
if 3 in valores:
    print(f'O número 3 aparece na {valores.index(3) + 1}° posição.')
else:
    print('O número 3 aparece não foi digitado em nenhuma posição.')
print('O valor par digitado foi ',end='')
for t in valores:
    if t % 2 == 0:
        print(f'{t}',end=' ')
