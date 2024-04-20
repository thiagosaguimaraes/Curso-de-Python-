# Esse abaixo foi para ver o fatorial só que com o for
'''num = int(input('Digite o número cujo o qual você deseja ver seu fatorial: '))
multi = 1
for f in range(num, 0, -1):
    multi = multi * f
    print(f'{f}',end=' x ' )
print(f'\nO fatorial de {num} é {multi}.')'''

# Esse foi para ver factorial usando um biblíoteca
'''from math import factorial
num = int(input('Digite um número: '))
f = factorial(num)
print(f'O fatorial de {num} é {f},')'''

# Esse é o que eu fiz, todo errado e fulera
'''num = 0
multi = 1
produto = multi * num
batata = 1
while num != 1: 
    num = int(input('Digite o número cujo o qual você deseja ver seu factorial: '))
    print(f'{num}! {num} x {num-batata}' )
    batata += -1
print(f'\nO fatorial e {num} é {produto}.')'''

# Esse é o que o guanabara fez, bolado
from time import sleep
n = int(input('Digite um número: '))
c = n
f = 1
print('Calculando...')
sleep(2)
print('5! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
