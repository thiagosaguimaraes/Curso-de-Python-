nome = str(input('Digite seu nome completo: ')).strip().title()
nomes = nome.split()
print('Bom dia, prazer em te conhecer.')
print(f'Seu primeiro nome é {nomes[0]}')
print(f'Seu último nome é {nomes[len(nomes)-1]}')
