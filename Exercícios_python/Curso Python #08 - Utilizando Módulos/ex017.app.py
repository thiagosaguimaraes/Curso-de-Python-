#from math import pow, sqrt
#b = float(input('Qual o comprimento do cateto oposto? '))
#c = float(input('Qual o comprimento do cateto adjacente? '))
#a = sqrt(pow(b,2) + pow(c,2))
#print(f'\nA hipotenusa vai medir {a:.2f}')

#Ou

#b = float(input('Qual o comprimento do cateto oposto? '))
#c = float(input('Qual o comprimento do cateto adjacente? '))
#print(f'\nA hipotenusa vai medir {(b ** 2 + c**2) ** (1/2):.2f}')

#Ou a melhor, por ser mais simples e mais fácil

from math import hypot
b = float(input('Qual o comprimento do cateto oposto? '))
c = float(input('Qual o comprimento do cateto adjacente? '))
print(f'\nA hipotenusa vai medir {hypot(b,c):.2f}')
