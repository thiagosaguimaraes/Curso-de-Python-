salário = float(input('Qual o seu salário? R$ '))
prc1 = salário + (salário * 10 / 100)
prc2 = salário + (salário * 15 / 100)
if salário > 1250:
    print(f'Parabéns você teve um aumento no seu salário de 10%, seu salário atual é de R$ {prc1:.2f}')
else:
    print(f'Parabéns você teve um aumento no seu salário de 15%, seu salário atual é de R$ {prc2:.2f}')
