#Esse foi do Guanabara também, esse while tá me ferrando, mas vo vencer essa porra
#-POR QUE UM DIA VOU SER UM PROGRAMADOR SÊNIOR
print('=' * 15)
print('Sequência de Fibonacci')
print('=' * 15)
num = int(input('Quantos termos deseja ver? '))
t1 = 0
t2 = 1
print('~' * 15)
print(f' {t1} ➞  {t2} ➞ ', end='')
cont = 3
while cont <= num:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f' {t3} ➞ ', end='')
    cont += 1
print(' Fim')
print('~' * 15)
