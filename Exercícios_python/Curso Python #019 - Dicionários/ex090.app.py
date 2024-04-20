while True: 
    livro = {}
    livro['nome'] = input('Nome do aluno: ').capitalize().strip()
    livro['média'] = float(input(f'Média de {livro["nome"]}: '))
    if livro['média'] >= 7:
        livro['situação'] = 'Aprovado'
    elif 5 <= livro['média'] < 7:
        livro['situação'] = 'Recuperação'
    else:
        livro['situação'] = 'Reprovado'
    print('=-' * 30)
    for k, v in livro.items():
        print(f'{k}: {v}')
    livro.clear()
    print('=-' * 30)
    while True:
        soun = input('Quer continuar com o programa? [S/N] ').upper().strip()[0]
        if soun in 'SN':
            break
    print('=-' * 30)
    if soun == 'N':
        break
print('=-' * 30)
