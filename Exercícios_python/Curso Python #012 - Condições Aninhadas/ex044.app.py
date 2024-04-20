print('-=-' * 20)
print(f'{" TSG Informática ":=^50}')
preço = float(input('Preço das compras: R$'))
pagamento = int(input('''Digite:
[ 1 ] à vista dinheiro/cheque
[ 2 ] a vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual a opção?  '''))

print('-=-' * 20)

if pagamento == 1:
    print(
        f'Pagamento a vista te garante 10% de desconto, o valor de sua compra agora é R${preço - (preço * 10 / 100):.2f}\n')

elif pagamento == 2:
    print(
        f'Pagamento a vista no cartão te garante 5% de desconto, o valor de sua compra agora é R${preço - (preço * 5 /100):.2f}\n')

elif pagamento == 3:
    print(f'Sua compra será parcelada em 2x de R${preço / 2:.2f} sem juros.')

elif pagamento == 4:
    juros = int(input('Em quantas vezes você quer parcelar sua compra? '))
    print(f'Sua compra será parcelada em {juros}x de R${preço / juros:.2f} com juros.\nSua compra de R${preço:.2f} ficara com o custo final de R${preço +(preço * 20 / 100):.2f}.')

else:
    print('''Erro...
    Escolha uma opção valida!'''.center(50))
print('-=-' * 20)
