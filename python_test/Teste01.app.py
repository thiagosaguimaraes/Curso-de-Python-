'''nome = input('Qual é seu nome?')
print('Olá', nome+'!', 'Bom dia,prazer em te conhece')

dia = input('Em que dia você nasceu?')
mes = input('Em que mês você nasceu?')
ano = input('Em que ano você nasceu?')

print('Você nasceu no dia', dia, 'de', mes, 'de', ano+',certo?')

x = int(input('Diga um numero!'))
y = int(input('Diga outro número!'))

print('A soma dos seus números é igual a', x + y)'''

#s = 'prova de python'
# print(len(s))

#num = int(input('Digite a quantidade de dinheiro que você tem:'))
#print(f'Você tem R${num:.2f}')

cont = 0
trigo = 1
while True:
    cont += 1
    if cont == 1:
        s = trigo
        print(f'Na {cont}° casa sera {trigo} semente ')
    else:
        s += trigo
        trigo += trigo
        print(f'Na {cont}° casa são {trigo} sementes ')
    if cont == 64:
        break
print(f'Ao total serão {s} sementes de trigo')
