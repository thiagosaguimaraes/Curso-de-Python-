texto = 'Olá, universo!'
print(f'Texto normal: {texto}')
print(f'Escolendo um caractere: {texto[5]}')
print(f'Com intervalo: {texto[5:9]}')
print(f'A partir de um ponto: {texto[2:]}')
print(f'Até um ponto: {texto[:9]}')
print('\n')
texto = '         Olá, universo!'
print(f'Apagando espaços no começo: {texto.strip()}')
print(f'Tamanho da string: {len(texto)}')


nome = 'joao silva santos'
print(nome.title())

print(nome.replace('santos', 'soares'))


print('A casa \'amarela\'')
print('Som do sistema: \a')

txtA = 'Código'
txtB = 'Nome'
txtC = 'email'
print(f'{txtA:<20}:: {txtB:^20} :: {txtC:>20}')

frase = 'Curso em Vídeo Python'
print(f'quantas vezes aparece a letra \'o\': {frase.count('o')}')
print(f'Vai dizer onde começou: {frase.find('deo')}')
print(f'Existe ’Curso’ em frase?”: {'Curso' in frase }') # as respostas podem ser “true” ou “false”
print(f'Vai substituir Python por Android: {frase.replace('Python','Android')}')
print(f'Deixa a string maiuscula: {frase.upper( )}')
print(f'Deixa a string em minúscula: {frase.lower( )}')
print(f'Coloca tudo na frase para minúsculo, exceto pela 1° letra que é passada para maiuscula: {frase.capitalize( )}')
print(f'Coloca a primeira letra de cada palavra para maiúscula: {frase.title( )}')
print(f'Elimina espaços vazios desnecessários, no início e no final da string: {frase.strip( )}')
print(f'Elimina espaços vazios desnecessários no final da string: {frase.rstrip( )}')
print(f'Elimina espaços vazios desnecessários no começo da string: {frase.lstrip( )}')
  

print(f'Gera uma lista com todas as palavras de uma cadeia de caracteres: {frase.split( )}')

frase.split()
print(f'Para juntar strings, no caso para as que passaram pelo split: {'-'.join(frase)}')


print(f'Se você quiser que seja um espaço normal é só: {' '.join(frase)}')


# frase = 'Curso em Vídeo Python'
# dividido = frase.split()
# print(dividido[2][3])


