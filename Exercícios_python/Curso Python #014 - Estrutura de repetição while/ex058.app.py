'''from random import randint
from time import sleep
h = 0
m = 1
r = 0
print('Você vai jogar um jogo com a maquina! Ele vai escolher um número de 0 a 10 e você tenta adivinha-lo')
while h != m:
    h = int(input('Escolha um número de 0 a 10: '))
    m = randint(0, 10)
    r += 1
    print('PROCESSANDO......')
    sleep(2)
    print(f'Você escolheu o número {h} e maquina escolheu o número {m}.')  
    if h != 0 and h != 1 and h != 2 and h != 3 and h != 4 and h != 5:
        print('É um número de 0 a 5 cabeça!\n')   
    elif h == m:
        print(f'Parabéns você acertou! Aconteceram {r} rodadas até você ganhar.\n')'''

from random import randint
computador = randint(1,10)
print('Oi, sou seu computador e acabei de pensar em um número entre 0 e 10')
print('Será que você consegue advinha-lo?')
acertou = False 
palpites = 0
computador = randint(0, 10)
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez.')
        elif jogador > computador:
            print('Menos...Tente mais uma vez.')
print(f'Você conseguiu acertar com {palpites} palpites, parabéns')
