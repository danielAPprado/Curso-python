from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),)
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO valor maximo foi de {max(numeros)}')
print(f'O valor minimo foi de {min(numeros)}')
