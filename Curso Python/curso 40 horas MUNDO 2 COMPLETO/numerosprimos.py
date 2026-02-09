num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
        print('\033[34m', end=' ')
    else:
        print('\033[30m', end=' ')
    print('{}'.format(c), end='')
print('\nO número {} foi divisivel por {} números'.format(num, tot))
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')