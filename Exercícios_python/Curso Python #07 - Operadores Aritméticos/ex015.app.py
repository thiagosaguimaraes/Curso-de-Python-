dias = int(input('Por quantos dias você alugou o carro? '))
quilômetros = int(
    input('Quantos quilômetros você rodou com o carro alugado? Km '))
print(
    f'O total que você tem que pagar é R${(dias * 60) + (quilômetros * 0.15):.2f}')
