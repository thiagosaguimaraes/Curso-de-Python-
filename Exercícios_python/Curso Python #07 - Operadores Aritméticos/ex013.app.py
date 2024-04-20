#s = float(input('Qual o seu sálario? R$'))
#print(f'Seu sálario é R${s:.2f}, com 15% de aumento fica R${s + (s * 15 /  100):.2f}')

p = float(input('Qual o preço do produto atual? R$'))
av = float(input('Qual a porcentagem de desconto ao compra-lo a vista? '))
prc = float(input('Em quantos porcento aumenta o preço ao compra-lo pareceladamente? ' ))

print(f'''Seu produto custa atualmente R${p} 
A vista ele custa R${p - (p * av /  100)} 
Parceladamente ele custa R${p + (p * prc /  100)}''')
