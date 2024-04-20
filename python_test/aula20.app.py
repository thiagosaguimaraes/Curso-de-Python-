# Fiz essa função pois séria uma tarefa repetitiva e chata então surgi o "separador"
def sep():
    print('#' * 60)


# Escrevendo algo repetitivo sem usar uma função
print('Sem uso da função')

print('-' * 20)
print('Batata')
print('-' * 20)

print('-' * 20)
print('Biscoito')
print('-' * 20)

print('-' * 20)
print('Banana')
print('-' * 20)

sep()

# Agora usando uma função, ocorre o mesmo resultado porém a construção é mais rápida

# Tem que ter 2 linhas de espaço entre a declaração da função, o 'def', do resto do código


def lin():
    print('-' * 20)


print('Usando a função "lin"')

lin()
print('Batata')
lin()

lin()
print('Biscoito')
lin()

lin()
print('Banana')
lin()

sep()

# Aqui é eu fazendo a função ter um parametro, eu consigo interagir com ela,
# escolher o que acontece quando uso ela, nesse caso é como se tivesse criado uma função que você pode
# escrever dento dos parenteses i isso ir pra lá, muito loko

print('Usando a função titulo')


def title(txt):
    print('-' * 20)
    print(txt)
    print('-' * 20)


title('Biscoitinho de batata')

sep()

# Fazendo agora uma função de soma, é fácil fazer sem a função, mas só de exemplo
print('Usando a função soma:')


def soma(a, b):
    s = a + b
    print(f'{a} + {b} = {s}')


# Dá pra fazer do jeito convencional e assim o
soma(2, 2)
soma(a=3, b=3)
soma(b=5, a=5)

sep()

# Agora se ligue, isso a baixo é uma função com algo novo, o "empacotador", basicamente você pode
# Colocar o parametro mutavel, ou seja, aumenta ou diminui conforme o quanto você for precisar
# Essa função vai servir para contar quantos itens você colocou dentro da função:
print('Função para contar quantos números você coloco')
def contador(*num):
    print(f'Recebi os valores {num} e ao todo são {len(num)} valores') 
    

contador(1,2,3)
contador(4,5,6,7,8)
contador(9,10,11,12,13,14)    

sep()
# Agora basicamente uma função que dobra os valores dentro de uma lista:
print('Uma função que dobra os valores dentro de uma lista')
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [2, 4, 6, 8, 10]
print(valores)
dobra(valores)
print(valores)
