while True:
    num = int(input('Qual número deseja ver a tabuada? '))
    if num < 0:
        break
    for t in range(1, 11):
        print(f'{num} X {t:02d} = {num * t}')
print('Fim')