#ano = int(input('Qual o ano? '))
#bis = ano % 8
#if bis == 0:
 #   print(f'O ano de {ano} é bissexto.')

#else:
 #   print(f'O ano de {ano} não é um ano bissexto') 

from datetime import date
ano = int(input('Qual o ano? Coloque 0 para analisar o ano atual. '))

if ano == 0:
    ano = date.today().year

if ano % 4 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto.')

else:
    print(f'O ano de {ano} não é um ano bissexto') 
