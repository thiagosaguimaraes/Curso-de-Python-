#reta1 = float(input('Qual o comprimento do 1° segmento de reta? '))
#reta2 = float(input('Qual o comprimento do 2° segmento de reta? '))
#reta3 = float(input('Qual o comprimento do 3° segmento de reta? '))
#teste = (reta1 + reta2) > reta3
#if teste == True:
 #   print('Esses seguimentos de reta podem fazer um triangulo')
#else:
 #   print('Esses seguimentos de reta não podem fazer um triangulo')

reta1 = float(input('Qual o comprimento do 1° segmento de reta? '))
reta2 = float(input('Qual o comprimento do 2° segmento de reta? '))
reta3 = float(input('Qual o comprimento do 3° segmento de reta? '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Esses seguimentos de reta podem fazer um triangulo')
else:
    print('Esses seguimentos de reta não podem fazer um triangulo')
    