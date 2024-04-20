from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0 
for nv in range(1,8):   
    ano = int(input(f'Em que ano a {nv}° nasceu: '))
    idade = atual - ano 
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print(f'Ao todo temos {totmaior} pessoas maiores de idade e {totmenor} pessoas menores de idade')

   

