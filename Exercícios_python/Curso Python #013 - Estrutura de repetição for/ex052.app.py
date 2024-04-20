num = int(input('Digite um número: '))
total = 0
for p in range(1, num + 1):
    if num % p == 0:
        print('\033[32m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')

    print(p, end=' ')

if total == 2:
    print(
        f'\033[m\nO número {num} é divisível por somente {total} números, por isso ele é um NÚMERO PRIMO')

elif total == 1:
    print(
        f'\033[m\nO número {num} não é um número primo e nem um número composto, ele é especial.')

else:
    print(print(
        f'\033[\nm O número {num} foi divisível {total} vezes, por isso ele não é um NÚMERO PRIMO'))
