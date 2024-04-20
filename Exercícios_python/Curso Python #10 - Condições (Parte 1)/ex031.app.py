km = float(input('Qual a distancia do ponto A até o ponto B? '))
custo1 = km * 0.50
custo2 = km * 0.45
if km <= 200:
    print(
    f'A distancia sendo de {km} km, faz a passangem custar R$ {custo1:.2f}')
else:
    print(
     f'A distancia sendo de {km} km, faz a passangem custar R$ {custo2:.2f}')
