'''s = 'MF'
while s != 'M' and s != 'F':
    s = str(input('Qual o seu sexo? ')).upper().strip()[0]
    if s != 'M' and s != 'F':
        print('Isso não é genero catapimbas! Verifique o que tem de baixo de vossa roupa intima e volte!')
print('Compreensivel tenha um bom dia!')'''

#Essa batata feia ae em cima, é a minha resposta ;=;

s = str(input('Qual o seu sexo? ')).upper().strip()[0]
while s not in 'MmFf':
    s = input(('Isso não é genero catapimbas! Verifique o que tem de baixo de vossa roupa intima e digite seu sexo: '))#ISSO É ZOERA
print('Compreensivel tenha um bom dia!')
