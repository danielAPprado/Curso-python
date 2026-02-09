num = int(input('Digite um número para ver sua fatorial: '))
c = num
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('O número {} em fatorial é {}'.format(num, f))
