soma = 0
contador = 0
for np in range(1, 7):
    num = int(input(f'Digite o {np}° número: '))
    if num % 2 == 0:
        soma += num
        contador += 1 
print(f'Você digitou {contador} números pares e a soma entre eles é: {soma}')
