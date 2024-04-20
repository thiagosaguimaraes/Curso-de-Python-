import requests
from tkinter import *


def média():
    n1 = float(input('Escreva sua 1° nota:'))
    n2 = float(input('Escreva sua 2° nota:'))

    print(f'Sua média é {(n1+n2)/2}')


janela = Tk()
janela.title('Média de notas')

texto_introdução = Label(
    janela, text='Digite suas notas e aperte o botão para obter sua média.')
texto_introdução.grid(column=0, row=0)

#pergunta_média =

janela.mainloop()
