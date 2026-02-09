maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(c)))
    if c == 1:
        maior = c
        menor = c
    else:
       if peso > maior:
           maior = peso
       if peso < menor:
           menor = peso
print('O menor peso foi {}Kg e o maior foi {}Kg'.format(menor, maior))
