#cid = str(input('Em que cidade você nasceu?\n')).strip()
#print(cid[:5].upper() == 'SANTO')

#Acima é a solução do Guanabara, abaixo é a minha, cuja qual gostei mais

cidade = (input('Em que cidade você nasceu?\n')).strip().title()
lista = cidade.split()
print(cidade)
print(lista)

print(f'Analisando {cidade}: {"Santo" in lista[0]}')
