#from random import randint
#print('-=-' * 20)
# print('JOKENPÔ'.center(50))
#print('-=-' * 20)

# jogador = int(input('''Digite:
# [ 1 ] para tesoura
# [ 2 ] para papel
# [ 3 ] para pedra
# sua escolha: '''))
#maquina = randint(1, 3)

# if jogador == 1 and maquina == 2:
#    print("\nTESOURA VS PAPEL\nSua fiel tesoura picota o papel da maquina como se não fosse nada.\n")
# elif jogador == 1 and maquina == 3:
#    print('\nTESOURA VS PEDRA\nua fiel tesoura perece nas mãos da grande rocha da maquina.\n')
# elif jogador == 1 and maquina == 1:
#    print('\nTESOURA VS TESOURA\nSua tesoura e a da maquina entram em um combate infinito e futil pela eternidade.\n')

# elif jogador == 2 and maquina == 3:
#    print('\nPAPEL VS PEDRA\nSua grande folha sulfite A4 envolve o pedregulho da maquina e o sufoca.\n')
# elif jogador == 2 and maquina == 1:
#    print('\nPAPEL VS TESOURA\nSua folha sulfite é picotada pela monstruosa tesoura da maquina.\n')
# lif jogador == 2 and maquina == 2:
#    print('\nPAPEL VS PAPEL\nSua folha de papel e a da maquina entram em um combate futil e fazem papel de trouxa.\n')

# elif jogador == 3 and maquina == 1:
#    print('\nPEDRA VS TESOURA\nPor mais que a tesoura seja afiada ela não é párea para o pedregulho e é apedrejada até desmontar.\n')
# elif jogador == 3 and maquina == 2:
#    print('\nPEDRA VS PAPEL\nSeu pedregulho confiante de seu treinamento na escola de rochas, parte para cima do inimigo, porem ele não esperava que fosse encontrar seu nemesis, O PAPEL, é embrulhado e sufocado até a morte.\n')
# elif jogador == 3 and maquina == 3:
#    print('''\nPEDRA VS PEDRA\nAs grandes rochas raivosas e confiantes em sua vitoria, rolam na direção da outra, mas elas param a metros de distancia uma da outra:
#    -Pe...Pedrita? É você...?
#    -Rochão?
#    Eles se encontram no meio do campo de batalha e se abraçam
#    -Nunca pensei que fosse te ver de novo, eles me disseram que você tinha morrido de placa tectonica (Disse Rochão)
#    -Não, eles mentiram para fazer uma troca de combatentes com a maquina
#    -Que bom ver que está viva, antes não tinha nada a perder morrendo na arena, mas agora..... que você esta aqui, não preciso mais disso.
#    Eles se beijam e saem juntos do campo de batalha. Assim ocorrendo um empate.''')
# else:

# print('''ERRO...
# Escolha uma opção valida'''.center(50))
#print('-=-' * 20)

from random import randint
from time import sleep

print('-=-' * 20)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(1, 3)
placar_jogador = 0
placar_maquina = 0

for ppt in range(0, 3):

    jogador = int(input('''Faça sua escolha:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA 
    Qual a sua jogada? '''))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    print('-=-' * 20)
    if jogador == computador:
        resultado = 'EMPATE'

    if jogador == computador:
        resultado = 'EMPATE'

    elif jogador == 0 and computador == 1:
        resultado = 'MAQUINA VENCEU!'
        placar_maquina += 1
    elif jogador == 0 and computador == 2:
        resultado = 'JOGADOR VENCEU!'
        placar_jogador += 1
    elif jogador == 1 and computador == 2:
        resultado = 'MAQUINA VENCEU!'
        placar_maquina += 1
    elif jogador == 1 and computador == 0:
        resultado = 'JOGADOR VENCEU!'
        placar_jogador += 1
    elif jogador == 2 and computador == 0:
        resultado = 'MAQUINA VENCEU!'
        placar_maquina += 1
    elif jogador == 2 and computador == 1:
        resultado = 'JOGADOR VENCEU!'
        placar_jogador += 1

    else:
        print('Escolha opções válidas')

    print(f'O computador jogou {itens[computador]}')
    print(f'O jogador jogou {itens[jogador]}')
    print('-=-' * 20)
    print(f'{placar_jogador} X {placar_maquina}')
    print(resultado)
    print('-=-' * 20)
    sleep(2)
    if placar_jogador >= 2:
        print('VOCÊ FOI CAMPEÃO JOGADOR')
    if placar_maquina >= 2:
        print('A MAQUINA VOI CAMPEÃ')
