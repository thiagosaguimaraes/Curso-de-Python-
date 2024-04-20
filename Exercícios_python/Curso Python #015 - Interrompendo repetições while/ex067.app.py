while True:
    num = int(input('De qual número você deseja ver sua tabuada? '))
    print('=-' * 20)
    if num < 0:
        break
    for t in range(1,11):
        print(f'{num} x {t:2} = {t * num}')
    print('=-' * 20)

print('Tabuada encerrada, tenha um bom dia!')
