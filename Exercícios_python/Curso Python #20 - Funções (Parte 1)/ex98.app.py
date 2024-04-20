'''def contador():
    def sep():
        print('=-' * 20)


    # def contador():
    sep()
    print('Contando de 1 até 10 de 1 em 1: ')
    for c in range(1, 11):
        print(f' {c}', end='')
    print(' FIM!')

    sep()
    print('Contando de 10 até 1 de 2 em 2: ')
    for d in range(10, -1, -2):
        print(f' {d}', end='')
    print(' FIM!')

    sep()
    print('Agora você escolhe os parametros da contagem seu puto: ')
    i = int(input('Início:    '))
    f = int(input('Fim:       '))
    p = int(input('Passo:     '))

    if p == 0:
        p = -1
    sep()
    print(f'Contagem de {i} até {f} de {p*(-1)} em {p*(-1)}: ')

    if i > f:
        f = f - 1
        if p > 0:
            p = p * (-1)

        
    for per in range(i, f, p):
        print(f'{per} ', end='')
    print('FIM!')
    sep()
contador()'''

from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
        
    print('=-' * 20) 
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(2.5)
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont =+ p
        print('FIM')
    
    else: 
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')
        
# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('=-' * 20) 
print('Agora é a sua vez de personalisar a contagem: ')
ini = int(input('Número inicial: '))
fin = int(input('Número final: '))
pas = int(input('Passo: '))
contador(ini, fin, pas)