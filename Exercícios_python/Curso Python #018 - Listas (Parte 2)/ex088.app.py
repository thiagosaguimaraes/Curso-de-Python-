'''from random import randint
sorteio = []
dado = []
cont = 1
print('=-' * 30)
print('JOGA NA MEGA SENA'.center(50))
print('=-' * 30)
jogadas = int(input('Digite quantos jogos você quer gerar: '))
print(f'{"=" * 4} SORTEANDO {jogadas} JOGOS {"=" * 4}')
for jogos in range(0, jogadas+1):
    sorteio.append(dado[:])
    dado.clear()
    for sorteados in range(1,7):
        while True:
            aleatório = randint(1,60)
            if aleatório not in dado:
                dado.append(aleatório)
                break
            else:
                aleatório = randint(1,60)        
del(sorteio[0])
for jogos in sorteio:
    print(f'Jogo {cont:2} : {jogos}')
    cont += 1
print('=-' * 5, 'Boa sorte!', '=-' * 5)'''

# O meu é o de cima
# Esse é o do guanabara
from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print('       JOGA NA MEGA SENA       ')
print('-' * 30)
quant = int(input('Quanto jogos você qure que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear
    tot += 1
print('-=' * 3, f'Sorteando {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('=-' * 5, '< Boa sorte! >', '=-' * 5)
