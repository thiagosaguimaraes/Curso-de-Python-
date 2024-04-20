tracin = '=-' * 20
print(f'{tracin} CAIXA ELETRÔNICO {tracin}')
valor = int(input('Qual a quantia que seja sacar? R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        if céd == 20:
            céd = 10
        if céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print(f'{tracin} TRANSAÇÃO CONLUíDA {tracin}\n                                          Tenha um bom dia')
