num = cont = soma = maior = menor = 0
soun = 'batata'
while soun not in ('N'):
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    soun = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if cont == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f'Você digitou {cont} números e a média deles foi {soma / cont}')
print(f'O maior número foi {maior} e o menor foi {menor}')
print('Acabou\n:D')

