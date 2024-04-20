peso = float(input('Qual o seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura * altura or altura ** 2)
print(f'Seu IMC (indice de massa corporal) é {imc:.1f} kg/m2')
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso ideal.')
elif 30 > imc >= 25:
    print('Sobrepeso.')
elif 40 > imc >= 30: 
    print('Obesidade.')
elif imc => 40:
    print('Obesidade mórbida.')
