# A partir do momento que se iguala uma lista a outra o python cria um ligação,
# quando se altera uma se altera a outra
print('=-' * 30)
a = [2, 3, 4, 7]
b = a
b[2] = 8
print('Lista com tentativa de copiar outra lista, alterando o valor "a" se altera o valor b')
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Para criar a copia de uma lista
print('=-' * 30)
c = [8, 9, 5, 6]
d = c[:]
d[2] = 8
print('Lista da copia, altera a d sem alterar c')
print(f'Lista C: {c}')
print(f'Lista D: {d}')

print('=-' * 30)
# Isso é uma lista composta,
# basicamente uma lista composta é uma lista com uma ou mais listas dentro
galera = [['Thiago', 16], ['Mikaelly', 16], ['Railam', 18], ['Int', 17]]

# Quando dou print no [0] ele seleciona toda a 1° lista dentro da lista, no caso Thiago:
print('=-' * 30)
print('Selecionando meu nome e minha idade na lista composta:')
print(galera[0])


# No caso eu posso selecionar coisas expecificas dentro de cada uma dessas listas:
# como só o meu nome por exemplo
print('=-' * 30)
print('Selecionando só o meu nome na lista composta')
print(galera[0][0])

# Para mostrar cada lista dentro da lista:
print('=-' * 30)
print('Mostrando o conteúdo das listas dento da lista:')
for pessoa in galera:
    print(pessoa)

# Selecionando só os nomes das pessoas das listas dentro das listas
print('=-' * 30)
print('Mostrando só o nome das pessoas das listas dentro da lista:')
for pessoa in galera:
    print(pessoa[0])

# Mostrando os nomes e as idades de cada lista interna formatado:
print('=-' * 30)
print('Mostrando o nome e a idade das pessoas de cada lista de maneira formatada:')
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} de idade')

# Um dos jeitos de gerar um programa com listas compostas é fazendo uma lista de uso temporário,
# que tera seus dados passados para outra lista e sera limpa:
print('=-' * 30)
galerinha = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 2):
    dado.append(input('Qual o seu nome? '))
    dado.append(int(input('Quantos anos você tem? ')))
    galerinha.append(dado[:])
# É nescessário limpar a lista de dados temporária para não haver repetições na lista principal
    dado.clear()

# Fazendo um programinha que lê nomes e idades e diz quem e quantos maiores e menores de idade tem
print(galerinha)
for p in galerinha:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1

print(f'Temos {totmaior} maiores de idade e {totmenor} menores de idade')
