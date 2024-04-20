# Para identificar uma tupla é só usar chavez {}

# Declarando um dicionário:
from operator import itemgetter
from time import sleep
from random import randint
dicionário = dict()
dicinário = {}

# O diferencial dos dicionários é que com eles você pode denominar os índices
# como por exemplo:
livrin = {}
# Preguiça de ficar escrevendo "dicionário"
livrin = {'nome': 'Pedro', 'idade': 25}
# 'Pedro' é o valor e 'nome' é o identificador do elemento
print('=-' * 30)
print('Denominando identificadores')
print(livrin)
print(livrin['nome'])
print(livrin['idade'])

# Os dicionários não precisam do uso do '.append()' para adicionar algo é
# só o seguinte comando que ele faz isso autómaticamente
print('=-' * 30)
print('Adicionando elementos')
livrin['sexo'] = 'M'
# Vai criar o elemento 'sexo', vai colocar 'M' dentro dele, tudo altómaticamente
print(livrin)

# Removendo elementos de um dicionário
print('=-' * 30)
print('Removendo elementos')
del livrin['idade']
# Vai deletar o elemento 'idade' e o valor dele '25'
print(livrin)

# Vou criar um dicionário para guadar nomes de filmes:
filmes = {'titulo': 'Star Wars',
          'ano': 1977,
          'diretor': 'George Lucas'}
# A chave pode continuar em outra linha sem problemas, contanto que ela feche

# Para se referir a diferentes partes de um dicionário se é usado 3 nomes:

# Para printar somente os valores
# São os valores dentro dos índices
print('=-' * 30)
print('Printando os valores, as chaves e tudo')
print(filmes.values())
#resultado: dict_values(['Star Wars', 1977, 'George Lucas'])

# Para printar somente as 'keys'(chaves)
# São como se fossem os índices
print(filmes.keys())
#resultado: dict_keys(['titulo', 'ano', 'diretor'])

# Para printar tudo, tanto valores quantos keys
print(filmes.items())
#resultado: dict_items([('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George Lucas')])

# Esses elementos são muito úteis para laços e ifs

print('=-' * 30)
print('Um for com dicionário:')
for k, v in filmes.items():
    print(f'O {k} é {v}')

# Dá para usar em conjunto tuplas, listas e dicionários,
# mas é melhor usar só listas e dicionários,
# tendo em vista que tuplas são uma bosta :D
print('=-' * 30)
print('Fazendo uma locadora com dicionários e lista')
filmes1 = {'titulo': 'Star Wars',
           'ano': 1977,
           'diretor': 'George Lucas'}
filmes2 = {'titulo': 'Avengers',
           'ano': 2012,
           'diretor': 'Josh Whedon'}
filmes3 = {'titulo': 'Matrix',
           'ano': 1999,
           'diretor': 'Wachowski'}
locadora = []
locadora.append(filmes1)
locadora.append(filmes2)
locadora.append(filmes3)
print(locadora)
print(locadora[0]['ano'])
print(locadora[2]['titulo'])
print()
for l in locadora:
    print(f'{"=-" * 30}')
    for k, v in l.items():
        print(f'{k} é {v}')

lista = []
livro = {}
for b in range(0, 2):
    print()
    print('=-' * 30)
    livro['nome'] = str(input('Nome: ')).strip().capitalize()
    livro['idade'] = int(input('Idade: '))
    # O jeito de copiar com [:], não funciona com dicionários,
    # mas tem uma função interna só pra isso ".copy"
    lista.append(livro.copy())
print()
print('=-' * 30)
print(lista)

print('=-' * 30)
for l in lista:
    print('-' * 30)
    for k, v in l.items():
        print(f'{k}: {v}')
print('-' * 30)
# Para colocar um dicionário em ordem:
print('=-' * 30)
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = []
print('Resultados dos dados:')
sleep(1)
for k, v in jogo.items():
    print(f'{k}: {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=-' * 30)
print('  == RANKING DOS JOGADORES ==  ')
for i, v in enumerate(ranking):
    print(f'    {i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
