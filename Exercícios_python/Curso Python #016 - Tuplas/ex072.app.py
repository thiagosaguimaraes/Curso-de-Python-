'''mv = ('zero', 'um', 'dois', 'três', 'quatro',
      'cinco', 'seis', 'sete', 'oito',
      'nove', 'dez', 'onze',
      'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
      'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 1 a 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end=' ')
print(f'Você digitou o número {mv[num]}')'''

mv = ('zero', 'um', 'dois', 'três', 'quatro',
      'cinco', 'seis', 'sete', 'oito',
      'nove', 'dez', 'onze',
      'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
      'dezessete', 'dezoito', 'dezenove', 'vinte')
soun = 'batata'
while True:
    num = int(input('Digite um número de 1 a 20: '))
    if 0 <= num <= 20:
          print(f'Você digitou o número {mv[num]}')
          while True: 
            soun = input('Você quer continuar com o programa? [S/N] ').upper().strip()
            if soun in 'SN':
                  break             
            else:
                  print('Tente novamente.',end=' ')
    else:
          print('Tente novamente.', end=' ')  
    if soun == 'N':
          break
print("\nPrograma finalisado\n".center(20))
    
