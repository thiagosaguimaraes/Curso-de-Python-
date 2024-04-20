'''frase = input('Digite uma frase: ').upper().strip()
palavras = frase.split( )
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso} ')
if junto == inverso:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')'''

frase = input('Digite uma frase: ').upper().strip()
palavras = frase.split( )
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso} ')
if junto == inverso:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')
