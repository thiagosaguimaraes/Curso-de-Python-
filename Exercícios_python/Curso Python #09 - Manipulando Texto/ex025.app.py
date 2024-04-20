nome = str(input('Qual seu nome?\n')).title().strip()
banana = nome.split()
print(f'Seu nome tem Silva?\n{"Silva" in banana}')
