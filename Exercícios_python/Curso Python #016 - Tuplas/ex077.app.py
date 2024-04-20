palavras = ('Batata', 'Biscoito', 'Banana', 'Abacate')
print(f'{"=" * 50}')
print(f'{"Vogais das palavras":^50}')
print(f'{"=" * 50}')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos',end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')            
