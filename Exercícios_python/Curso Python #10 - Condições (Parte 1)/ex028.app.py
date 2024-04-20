from random import randint
from time import sleep
print('Você vai jogar um jogo com a maquina! Ele vai escolher um número de 0 a 5 e você tenta adivinha-lo')
h = int(input('Escolha um número de 0 a 5: '))
m = randint(0, 5)
print('PROCESSANDO......')
sleep(3)
print(f'A maquina escolheu o número {m} e você escolheu {h}, ou seja...')

if h == m:
    print('Parabéns você acertou!')
else:
    print('Errou troxa')
