print('-=-' * 40)
print('10 PRIMEIOROS TERMOS DE UMA PA'.center(50))
print('-=-' * 40)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f' {termo} ➡ ',end='')
        termo += razão
        contador += 1
    print(' Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Processo finalizado, foram mostrados {total} termos')
    