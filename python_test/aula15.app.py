# Esse é o jeito que normalmente foi feito até agora:

'''cont = 1
while cont <=10:
    print(cont,end=' -> ')
    cont += 1
print('Acabou')'''

# Esse aqui tem a mesma funcionalidade que o de cima, porem ele não tem um teste lógico para a sua parada e é infinito:

'''cont = 1
while True:
    print(cont,end=' -> ')
    cont += 1
print('Acabou')'''

# Tem um jeito de parar essa estrutura de repetição sem um teste lógico, usando um break em em uma condição, como:

'''cont = 1
while True:
    print(cont,end=' -> ')
    cont += 1
    if cont == 11:
        break
print('Acabou')'''

nome = 'Jóse'
print(f'batata {nome:=<20} batata')
