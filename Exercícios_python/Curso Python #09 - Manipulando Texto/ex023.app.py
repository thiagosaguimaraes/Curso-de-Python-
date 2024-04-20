#número = str(input('Digite um número de 0 a 9.999 : '))
#print(f'''Analisando o número {número} :
#Milhar: {número[0]}
#Centena: {número[1]}
#Dezena: {número[2]}
#Unidade: {número[3]}''')

#Essa porra de cima, não funciona

número = int(input('Digite um número de 0 a 9.999 : '))
print(f'''Analisando o número {número} :
Unidade: {número // 1 % 10}
Dezena: {número // 10 % 10}
Centena: {número // 100 % 10}
Milhar: {número // 1000 % 10}''')
