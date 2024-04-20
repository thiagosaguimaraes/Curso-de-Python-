pv = float(
    input('Qual o preço do produto que você gostária de adicionar o desconto? R$'))
pn = pv - (pv * 5 / 100)
print(
    f'Seu produto que custa R${pv:.2f}, com 5% de desconto ficara custando R${pn:.2f}\n')

