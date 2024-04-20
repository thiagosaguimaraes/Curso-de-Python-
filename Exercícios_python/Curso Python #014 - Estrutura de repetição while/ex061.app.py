'''print('=' * 40)
print('10 PRIMEIOROS TERMOS DE UMA PA'.center(50))
print('=' * 40)
termo1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = termo1 + (10-1) * razão
for p in range(termo1, décimo + razão, razão):
    print(p, end=' ➜  ')
print('Fim')'''

print('-=-' * 40)
print('10 PRIMEIOROS TERMOS DE UMA PA'.center(50))
print('-=-' * 40)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
contador = 1
while contador <= 10:
    print(f' {termo} ➡ ',end='')
    termo += razão
    contador += 1
print(' Fim')
