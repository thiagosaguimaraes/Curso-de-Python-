'''números = []
impar = []
par = []
for n in range(1,8):
    num = int(input(f'Digite o {n}° número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
        
números.append(impar[:])
números.append(par[:])
impar.clear
par.clear

print(f'Você digitou {len(números[0])} números ímpares e são eles: {números[0]}')
print(f'Você digitou {len(números[1])} números pares e são eles: {números[1]}')'''
    
'''números = [[], []]
dado = 0
for c in range(1,8):
    dado = int(input(f'Digite o {c}° número: '))
    if dado % 2 == 0:
        números[0].append(dado)
    else:
        números[1].append(dado)
números[0].sort()
números[1].sort()
print('=-' * 30)
print(f'Você digitou {len(números[0])} números pares e são eles: {números[0]}')
print(f'Você digitou {len(números[1])} números ímpares e são eles: {números[1]}')
print('=-' * 30)'''

'''lista = []
par = []
impar = []
cont = cont_par = cont_impar = 0
while True:
    print('=-' * 30)
    n = int(input('Digite um número: '))
    lista.append(n)
    cont += 1
    if n % 2 == 0:
        par.append(n)
        cont_par += 1
    else:
        impar.append(n)
        cont_impar += 1
    while True:
        print('=-' * 30)
        soun = input(
            'Você quer continuar com o programa? [S/N] ').strip().upper()[0]
        if soun in 'SN':
            break
    if soun in 'N':
        break
lista.sort()
par.sort()
impar.sort()
print(f'Você digitou {cont} valores e eles são: {lista}')
print(f'Você digitou {cont_par} valores pares e eles são: {par}')
print(f'Você digitou {cont_impar} valores impares e eles são: {impar}')'''

###########################

lista = []
par = []
impar = []
cont = cont_par = cont_impar = 0
while True:
    print('=-' * 30)
    n = int(input('Digite um número: '))
    lista.append(n)
    cont += 1
    
    while True:
        print('=-' * 30)
        soun = input(
            'Você quer continuar com o programa? [S/N] ').strip().upper()[0]
        if soun in 'SN':
            break
    if soun in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
        cont_par += 1
    elif v % 2 == 1:
        impar.append(v)
        cont_impar += 1

print(f'Você digitou {cont} valores e eles são: {lista}')
print(f'Você digitou {cont_par} valores pares e eles são: {par}')
print(f'Você digitou {cont_impar} valores impares e eles são: {impar}')
