from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
if idade <= 9:
    ct = "MIRIM"
elif idade <= 14:
    ct = "INFANTIL"
elif idade <= 19:
    ct = "JUNIOR"
elif idade <= 25:
    ct = "SÊNIOR"
else:
    ct = "MASTER"
print(f'Com a idade de {idade} anos você fica na categoria {ct}')
