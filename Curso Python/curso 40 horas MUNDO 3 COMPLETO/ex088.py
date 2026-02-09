from random import randint
from time import sleep
lista = []
jogos = []
n = int(input('Quantos jogos deseja fazer? '))
tot = 1
while tot <= n:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, v in enumerate(jogos):
    print(f'Jogo {i+1}: {v}')
    sleep(1)
