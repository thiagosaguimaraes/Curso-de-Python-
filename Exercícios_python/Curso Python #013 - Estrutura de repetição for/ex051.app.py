print('=' * 50)
print('10 PRIMEIOROS TERMOS DE UMA PA'.center(50))
print('=' * 50)
termo1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = termo1 + (10-1) * razão
for p in range(termo1, décimo + razão, razão):
    print(p, end=' ➜  ')
print('Fim')
