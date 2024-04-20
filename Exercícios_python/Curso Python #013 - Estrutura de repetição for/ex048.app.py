soma = 0
contador = 0
for t in range(1, 501, 2):
    if t % 3 == 0:
        soma += t #or soma = soma + t
        contador += 1 #or contador = contador + 1 
print(f'A soma de todos os {contador} números solicitados é {soma}')
