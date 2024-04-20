n = input('Digite algo:')

print('Segue as informações sobre o que você digitou')
print('Seu tipo primitivo', type(n))
print('É um número?', n.isnumeric())
print('Está em letras maiusculas?', n.isupper())
print('É letra?', n.isalpha())
print('É alpha, n.isalnum()')
print('É decimal?', n.isdecimal())
