from time import sleep
opc = 0
print('-=-' * 15)
print('Digite dois números:')
n1 = float(input('1° número: '))
n2 = float(input('2° número: '))
print('=-=' * 15)
while opc != 5:
    print('Pressione:\n[ 1 ] para Somar\n[ 2 ] para Multiplicar\n[ 3 ] Maior\n[ 4 ] para Novos números\n[ 5 ] para Sair do programa')
    opc = int(input('Sua opção: '))
    if opc == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif opc == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif opc == 3:
        #print(f'O maior número entre {n1} e {n2} é {max(n1,n2)}')
        if n1 > n2:
            print(f'O número {n1} é maior que {n2}.')
        elif n1 < n2:
            print(f'O número {n2} é maior que {n1}.')
        elif n1 == n2:
            print(f'O número {n1} é igual ao número {n2}.')
    elif opc == 4:
        print('Digite os novos números')
        n1 = float(input('1° número: '))
        n2 = float(input('2° número: '))
    elif 1 > opc > 5:
        print('Opção inválida, tente novamente.')
print('=-=' * 15)
print('Finalisando...')
print('-=-' * 15)
sleep(1)
print('Fim do progrma, volte sempre')
