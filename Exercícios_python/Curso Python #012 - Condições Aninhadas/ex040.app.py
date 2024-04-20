nota1 = float(input('Qual a 1° nota? '))
nota2 = float(input('Qual a 2° nota? '))
média = (nota1 + nota2) / 2
print(f'A média do aluno é {média}')
if média < 5.0:
    print('O aluno está reprovado.')
elif média >= 5.0 and média < 6.9:
    print('O aluno está em recuperação.')
elif média >= 7:
    print('O aluno está aprovado.')
