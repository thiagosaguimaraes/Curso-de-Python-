'''igual = '-' * 4
maior_idade = 0
nomevelho = 0
mulheres20 = 0
média = 0
for c in range(1, 5):
    print(f'{igual} {c}° Pessoa {igual}')
    nome = input('Nome: ').strip().capitalize()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    
    if c == 1:
        média += idade
    elif c == 2:
        média += idade
    elif c == 3:
        média += idade
    elif c == 4:
        média += idade

    if sexo == 'M':
        if c == 1:
            maior_idade = c
            nomevelho = nome
        else:
            if idade > maior_idade:
                maior_idade = idade
                nomevelho = nome

    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    
    if sexo != 'F' and sexo != 'M':
        print('Error, escolha uma opção válida.') 
                    
print('-=-' * 20)
print(f'A média de idade é de {média / c:.1f}')
print('-=-' * 20)
print(f'O homen mais velho tem {maior_idade} anos e o nome dele é {nomevelho}.')
print('-=-' * 20)
print(f'Ao todo são {mulheres20} mulheres com menos de 20 anos.')
print('-=-' * 20)'''

soma_idade = 0
média_idade = 0
maior_idade_homen = 0
nome_mais_velho = 0
total_mulher_20 = 0
for p in range(1, 3):
    print(f'---- {p}° Pessoa ----')
    nome = input('Nome: ').strip().capitalize()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    soma_idade += idade
    média_idade = soma_idade / 4
    
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homen:
        maior_idade_homen = idade
        nome_mais_velho = nome
    
    if sexo in 'Ff' and idade < 20:
        total_mulher_20 += 1

print(f'A média de idade é de {média_idade}')
print(f'O homen mais velho tem {maior_idade_homen} anos e o nome dele é {nome_mais_velho}.')
print(f'Ao todo são {total_mulher_20} mulheres com menos de 20 anos.')
