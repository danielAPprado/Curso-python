from random import randint
from time import sleep
numeros = []

def sorteia(lista):
    print(f'Sorteando valores: ', end='')
    for c in range(0, 5):
        num = randint(0, 9)
        lista.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.3)
    print('END')


def soma(lista):
    a = 0
    for n in lista:
        if n % 2 == 0:
            a += n
    print(f'A soma dos números pares é {a}')


sorteia(numeros)
soma(numeros)

