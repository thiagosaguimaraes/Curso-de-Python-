nome = str(input('Qual o seu nome completo?\n')).strip()
lista = nome.split()
#Primeiro = lista[0]
print(f'''Seu nome em letras minusculas é: {nome.lower()} 
Seu nome em letras maiusculas é: {nome.upper()}
Seu nome tem {len(nome) - nome.count(' ')} letras
Seu primeiro nome tem {len(lista[0])} letras''')
# Seu primeiro nome tem {len(Primeiro)} letras''')
