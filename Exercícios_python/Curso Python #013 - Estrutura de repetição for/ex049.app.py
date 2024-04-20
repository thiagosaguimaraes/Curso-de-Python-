'''print('-=-' * 20)
num = int(input('De qual número você pretende ver a tabuada? '))
final = (num * 10) + num
contador = 0
print('-=-' * 20)
for t in range(num, final, num):
    contador += 1
    print(f"{num:2}  x  {contador:2}  =  {t:2}")
print('-=-' * 20)'''

#Esse abaixo foi a solução do guanabara, a de cima foi a minha.

print('-=-' * 20)
num = int(input('De qual número você pretende ver a tabuada? '))
print('-=-' * 20)
for c in range(1, 11):
    print(f'{num} x {c:2} = {num * c}')
print('-=-' * 20)
