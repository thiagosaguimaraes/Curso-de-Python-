from random import shuffle  
al1 = input('1° aluno: ')
al2 = input('2° aluno: ')
al3 = input('3° aluno: ')
al4 = input('4° aluno: ')
lista = [al1, al2, al3, al4]
print(lista)
shuffle(lista)
print(f'A ondem da apresentação será: {lista}')
