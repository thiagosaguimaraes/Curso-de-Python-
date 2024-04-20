pessoa = {}
pessoas = []
cont = 1
cut = 0
média = 0
print('=-' * 30)
while True:
    pessoa.clear()
    print(f'   ==== {cont}° pessoa ====   ')
    cont += 1
    pessoa['Nome'] = input('Nome: ').strip().capitalize()

    while True:
        pessoa['sexo'] = input('Sexo: ').strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('Por favor digite M ou F. ', end='')

    pessoa['Idade'] = int(input('Idade: '))
    média += pessoa['Idade']       
    pessoas.append(pessoa.copy())
    print('=-' * 30)
    while True:
        soun = input(
            'Quer continuar com o programa? [S/N] ').strip().upper()[0]
        if soun in 'SN':
            break
    print('=-' * 30)
    if soun == 'N':
        print(pessoa.items())
        print(pessoas)
        break
print('')
print(f'A) O programa cadastrou {len(pessoas)} pessoas')
print(f'B) A média de idade é {média / len(pessoas):5.2f} anos ')
print(f'C) As mulheres cadastradas foram: ',end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["Nome"]}',end=' ')
print()

print(f'D) Lista de pessoas que tem a idade acima da média: ',end='')
for p in pessoas:
    if p['Idade'] >= média / len(pessoas):
        print()
        for k, v in p.items():
            print(f'{k}: {v}')
print()        
print('PROGRAMA ENCERRADO'.center(50))
