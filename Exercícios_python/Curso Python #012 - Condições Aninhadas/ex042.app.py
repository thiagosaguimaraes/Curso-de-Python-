reta1 = float(input('Qual o comprimento do 1° segmento de reta? '))
reta2 = float(input('Qual o comprimento do 2° segmento de reta? '))
reta3 = float(input('Qual o comprimento do 3° segmento de reta? '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    if reta1 == reta2 == reta3:
        triangulo = 'EQUILÁTERO'
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        triangulo = 'ISÓCELES'
    elif reta1 != reta2 != reta3 != reta1 or reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
        triangulo = 'ESCALENO'
    print(f'Esses seguimentos de reta podem fazer um triangulo e ele será um triangulo {triangulo}')

else:
    print('Esses seguimentos de reta não podem fazer um triangulo')



#if reta1 == reta2 == reta3:
#    print('E esse triangulo formado será um triangulo EQUILÁTERO')
#elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
#    print('E esse triangulo formado será um triangulo ISÓCELES')
#elif reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
#    print('E esse triangulo formado será um triangulo ESCALENO')
