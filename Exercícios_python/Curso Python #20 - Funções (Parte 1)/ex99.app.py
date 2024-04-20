from time import sleep


def maior(*num):
    max = cont = 0
    print('=-' * 30)
    print('Analisando valores...')
    for n in num:
        sleep(0.5)
        print(f'{n} ', end='', flush=True)
        if cont == 0:
            max = n
        else:
            if n > max:
                max = n 
        cont += 1
    sleep(1)
    print(f'Foram informados {cont} valores ao todo\nO maior deles foi {max}', flush=True)
    print('=-' * 30)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
