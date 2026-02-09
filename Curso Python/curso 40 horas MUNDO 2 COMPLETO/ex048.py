soma = 0
count = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        count +=1
        soma += c
print('A soma dos números é {}'.format(soma))
print('A quantidade de números é {}'.format(count))