#from datetime import date
#ano = int(input('Em que ano você nasceu? '))
#idade = date.today().year - ano
#if idade < 18:
#    print(f'Você tem {idade} anos, ainda não alcançou a idade necessária para servir, faltam {(idade - 18) * -1} ano')
#    print(f'Seu alistamento será no ano de {}')
#elif idade == 18:
#    print(f'Você tem {idade} anos, já alcançou a idade necessária para servir, venha rápido, temos muito mato para capinar!')
#elif idade > 18 and idade < 36:
#    print(f'Você tem {idade} anos, já tinha que ter se alistado no exercito a muito tempo, está {idade - 18} anos atrasado')

#Tem algo errado nessa porra ae embaixo, tenho quase certeza
from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = (nasc - atual) * -1
saldo = (idade - 18) * -1

print(f'Você tem {idade} ano(s)')

if idade < 18:
    ano = atual + saldo
    print(f'Ainda não tem a idade nescessária para servir, ainda falta(m) {saldo} ano(s), você servira no ano de {ano} ')

elif idade == 18:
    print('Já tem a idade nescessária para servir, venha o mais rapido possivel!')

elif idade > 18:
    ona = atual - saldo
    print(f'Está atrasado para servir o exercito, você deveria ter servido no ano de {ona}')
