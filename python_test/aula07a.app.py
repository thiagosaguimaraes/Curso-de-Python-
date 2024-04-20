n1 = int(input('Digite um númeoro:'))
n2 = int(input('Digite outro número:'))

s = n1+n2
p = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print(f'A soma é igual a {s} \n o produto é {p} \n a divisão é {d:.3f},', end=' ')
print(f'a divisão inteira é {di} \n a exponenciação é {e}')
