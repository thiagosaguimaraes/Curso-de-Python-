# Uma lista fica entre colchetes
num = [2, 5, 9, 1]
print('=-' * 50)
print('Lista normal sem alterações')
print(num)

# É possivel substituir valores nas listas, listas são mutaveis
num[2] = 3
print('=-' * 50)
print('Lista com valor substituido')
print(num)

# Para adicionar valores em listas
num.append(7)
print('=-' * 50)
print('Lista com valor adicionado')
print(num)

# Para colocar em ordem
num.sort()
print('=-' * 50)
print('Lista com valores ordenados do menor para o maior')
print(num)

# Para colocar do maior para o menor
num.sort(reverse=True)
print('=-' * 50)
print('Lista com valores ordenados do maior para o menor')
print(num)

# Para saber quantos elementos tem uma lista
print('=-' * 50)
print('Número da quantidade de elementos da lista')
print(f'A lista tem {len(num)} elementos')

# Para inserir um valor a lista e jogar o que estava nesta posição a direita
num.insert(2, 0)
# Na posição 2 inserir o valor 0
print('=-' * 50)
print('Lista com valor adicionado em um lugar especifico')
print(num)

# Para remover o último elemento de uma lista
print('=-' * 50)
num.pop()
print('Lista com o último elemento removido')
print(num)

# Para remover um elemento na lista
print('=-' * 50)
num.pop(2)
print('Lista com valor da posição espécifica removida')
print(num)
# Eliminar o que está na posição 2

num.insert(2, 3)
print('=-' * 50)
print(num)
# Remove um número de sua escolha, mesmo se tiver mais de um desse número,
# ele elimina só o 1° dele
num.remove(3)
# Se tentar remover algo que não está na lista o programa ira dar  erro
print('Lista com valor espécifico removido')
print(num)

# Para excluir um valor cujo qual não se tem conhecimento se ele está na lista ou não
if 5 in num:
    print('=-' * 50)
    print('Lista com número 5 removido com um teste para saber se ele tá na lista')
    num.remove(5)
    print(num)
else:
    print('Não achei 5 aqui n doido')

# 2 meios para fazer uma lista vazia
valores = []
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
print('=-' * 50)
print('lista do jeito feio')
print(valores)
# Para mostrar os valores bonitinho
# O enurate gera duas variáveis com as posições e dos valores nas listas
print('=-' * 50)
# Lendo valores pelo teclado e colocando dentro da lista
print('Lendo valores pelo teclado e colocando dentro de uma lista')
for cont in range(0, 3):
    valores.append(int(input('Digite um valor:')))

print('\nLista do jeito bonito')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

print('=-' * 50)
# A partir do momento que se iguala uma lista a outra o python cria um ligação,
# quando se altera uma se altera a outra
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Para criar a copia de uma lista
c = [8, 9, 5, 6]
d = c[:]
d[2] = 8
print('Lista da copia, altera a d sem alterar c')
print(f'Lista C: {c}')
print(f'Lista D: {d}')
