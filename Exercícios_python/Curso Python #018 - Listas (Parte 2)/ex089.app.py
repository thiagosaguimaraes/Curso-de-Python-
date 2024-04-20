from time import sleep
meta = []
dado = []
cont = 1
print('=-' * 10, 'Boletins', '=-' * 10)

while True:
    print('-' * 5, f'ALUNO {cont}', '-' * 5)
    cont += 1
    nome = input('Nome: ').capitalize().strip()
    dado.append(nome)
    n1 = float(input('Nota 1: '))
    dado.append(n1)
    n2 = float(input('Nota 2: '))
    dado.append(n2)
    meta.append(dado[:])
    dado.clear()
    print('=-' * 10)
    while True:
        soun = input('Quer continuar? [S/N] ').upper().strip()[0]
        if soun in 'SN':
            print('=-' * 10)
            break
    if soun == 'N':
        break
print('=-' * 25)
print(f'{"N°.":<4} {"Nome":<10} {"Média":>8}')
print('-' * 50)
cont = 0
for pessoas in meta:
    média = (pessoas[1]+pessoas[2]) // 2
    cont += 1
    print(f'{cont:<4}{pessoas[0]:<10}{média:>8.1f}')
print('-' * 50)


while True:
    aluno = int(input('Mostrar as notas de qual aluno? [999 para parar]: '))
    corresp = aluno - 1

    if aluno == 999:
        print('Finalizando...')
        sleep(1)
        break

    if corresp <= len(meta):
        print(
            f'Notas de {meta[corresp][0]} são [{meta[corresp][1]}, {meta[corresp][2]}]')
        print('-' * 50)
    else:
        print('Tente novamente. Digite o número corespondete ao do aluno. ', end='')
print({'>'*5}, 'VOLTE SEMPRE', {'<'*5})
