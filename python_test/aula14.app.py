'''for c in range(1,10):
    print(c)
print('Fim')

c = 1
while not c < 10:
    print(c)
    c += 1
print('Fim')

n = 1
while not n != 0:
    int(input('Digite um valor: '))
print('Fim')

n = 1
r = 'S'
while not r == 'S':
    int(input('Digite um valor: '))
    input('Quer continuar? [S/N]: ').upper()
print('Fim')'''

n = 1
par = impar = 0
num = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        num += 1  
        if n % 2 == 0:
            par += 1
        else:
            impar += 1        
print(f'Você digitou {num} números, {par} números pares e {impar} número impares')
print('Fim')