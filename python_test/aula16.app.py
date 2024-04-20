lanche = ('Batata', 'Biscoito', 'Banana', 'Pastel', 'Maminha')

print('=-' * 50)
print('Fome da porra')

print('=-' * 50)
#Esse só mostra as strings
for comida in lanche:
    print(f'Vo comer {comida}')
print('=-' * 50)
#Esse mostra as strings e sua posição
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('=-' * 50)
#Também mostra as strings e sua posição porém com outro metodo
# esse enumerate torna póssivel pegar a string e sua posição
for pos, comida in enumerate(lanche):
    print(f'Vo comer {comida} na posição {pos}')

#print(f'Uff, quase morri mas valeu a pena!')
print('=-' * 50)
#A função sorted ordena os elementros em ordem alfabetica
lanche = ('Batata', 'Biscoito', 'Banana', 'Pastel', 'Maminha')
print(sorted(lanche))
print('=-' * 50)
#Concatecnação de tuplas:
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(b + a)
print(c)
#O sorted também ordena os números do menor para o maior
print(sorted(c))
print(sorted(a + b))
print('=-' * 50)
c = (2, 5, 4, 5, 8, 1, 2)

#Quantos elementos tem na minha tupla?
print('=-' * 50)
print(len(c))
print('=-' * 50)

#Tem quantos números 5 na minha tupla?
print(c.count(5))
print('=-' * 50)

#Em que posição o número 5 aparece na minha tupla?
print(c.index(5))
#Mesmo tendo só dois cincos, só se mostra a posição do primeiro
print('=-' * 50)


#Para saber a posição do segundo:
print(c.index(5,1))
#Basicamente falando "Verifica se tem um 5 ae, mas só a paritir da posição 1"
print('=-' * 50)


# É possivel ter diferentes tipos de dados em uma tupla:
pessoa = ('Gustavo', 39, 'M', 99.88)

# A tupla é imutavel, só pode mudar o valor apagando-o,
# não se pode mudar o valor de um dos espaços no meio do programa

# É possivel se deletar uma tupla
del(pessoa)
print(pessoa)
print('Não dá resultado pq foi apagada')
