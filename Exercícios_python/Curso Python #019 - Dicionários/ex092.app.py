from datetime import date
pessoa = {}
ano_atual = date.today().year
pessoa['Nome'] = input('Nome: ').strip().capitalize()
nascimento = int(input('Ano de nascimento: '))
pessoa['Idade'] = ano_atual - nascimento
pessoa['Carteira de trabalho'] = int(
    input('Carteira de trabalho [0 não tem]: '))
if pessoa['Carteira de trabalho'] != 0:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    pessoa['aposentar'] = 35 - (ano_atual - pessoa['Ano de contratação'])
    anosaposen = pessoa['aposentar'] + pessoa['Idade']
print('=-' * 30)
for k, v in pessoa.items():
    if k == 'Salário':
        print(f'{k}: R${v:.2f}')
    elif k == 'aposentar':
        print(
            f'Faltam {v} anos para se aposentar, você se aposentara com {anosaposen} anos')
    else:
        print(f'{k}: {v}')
