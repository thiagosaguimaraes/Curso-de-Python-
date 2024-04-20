def escreva(msg):
    lin = len(msg) + 4
    print('~' * lin)
    print(f'  {msg}')
    print('~' * lin)

escreva('Batata')
escreva('Batata é mo delicia')
escreva('Batata é muito bom, puta merda')

frase = input('Escreva uma frase: ')
escreva(frase)
