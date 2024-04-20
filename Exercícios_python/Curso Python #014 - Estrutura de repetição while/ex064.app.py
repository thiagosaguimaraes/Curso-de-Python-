cont = soma = num = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    cont += 1
    if num != 999:
        soma += num
    else:
        cont = cont - 1
print(f'Você digitou {cont} números e a soma deles foi de {soma}')

#Ou

cont = soma = num = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:   
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma deles foi de {soma}')
