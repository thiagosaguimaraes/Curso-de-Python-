velocidade = float(input('Qual a velocidade do carro? '))
multa = (velocidade-80) * 7

if velocidade <= 80.00:
    print('Você tá limpo meu pareceiro, pode continuar.')

else:
    print(f'Você tá loko meu nobre, o limite de velocidade aqui é de 80 km por hora e você estava a {velocidade} km, tome uma multa de R$ {multa:.2f}.')
