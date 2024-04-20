lista = []
cont = 0
while True:
    print('=-' * 30)
    lista.append(int(input('Digite um número: ')))
    cont += 1
    while True:
        soun = input(
            'Você quer continuar com o programa? [S/N] ').strip().upper()[0]
        if soun in 'SN':
            break
        else:
            print('Tente novamente. ', end='')

    if soun == 'N':
        break
print('=-' * 30)
print(f'Você digitou {len(lista)} valores.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')
