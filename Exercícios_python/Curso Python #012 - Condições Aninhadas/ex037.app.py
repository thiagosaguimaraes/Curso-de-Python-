número = int(input('Digite um número inteiro: ').strip())
conversão = int(input('''Escolha qual a base de conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
sua escolha: ''').strip())
if conversão == 1:
    print(f'O número {número} convertido para binário é igual a {número:b}')
    #print(f'O número {número} convertido para binário é igual a {bin(número)[2:]}')
elif conversão == 2:
    print(f'O número {número} convertido para octal é igual a {número:o}')
    #print(f'O número {número} convertido para octal é igual a {oct(número)[2:]}')
elif conversão == 3:
    print(f'O número {número} convertido para hexadecimal é igual a {número:x}')
    #print(f'O número {número} convertido para hexadecimal é igual a {hex(número)[2:]}')
else:
    print('ERRO...'.center(50))
    print('Ecolha uma opção válida!'.center(50))
