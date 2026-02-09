print('-' * 50)
print('Sequência Fibonnaci')
print('-' * 50)
termos = int(input('Quantos termos você quer? '))
n1 = 0
n2 = 1
count = 3
print('{} - {} -'.format(n1, n2), end='')
while count <= termos:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count += 1
    print(' {} -'.format(n3), end='')
print('FIM')