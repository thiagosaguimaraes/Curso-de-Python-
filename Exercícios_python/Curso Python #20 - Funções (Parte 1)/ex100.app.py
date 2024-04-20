from random import randint
from time import sleep
números = []


def sorteio(lista):
    print('Sorteando 5 valores para a lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.7)
    print('FIM')


sorteio(números)


def somaPar(lista):
    soma = par = imp = 0
    for cont in lista:
        if cont % 2 == 0:
            soma += cont
            par += 1
        else:
            imp += 1
    print(f'Há {imp} números impar(es) e {par} números par(es), a soma de todos os números pares é {soma}')


somaPar(números)
