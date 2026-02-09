num = int(input('Digite um número que deseje a tabuada: '))
for c in range(1, 101):
    print('{} X {:2} = {}'.format(num, c, num*c))
    #print('')
