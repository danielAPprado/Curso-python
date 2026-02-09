from random import randint
numerom = randint(1, 10)
tentativas = 0
acertou = False
print('A maquina pensará num numero de 1 a 10, tente adivinha-lo')
while not acertou:
    numeroj = int(input('Digite o número o qual a maquina pensou: '))
    tentativas += 1
    if numeroj == numerom:
        acertou = True
    else:
        if numeroj < numerom:
            print('Maior...')
        else:
            print('Menor...')
print('Parabéns, você acertou! o número era {}. Você utilizou {} tentativas'.format(numerom, tentativas))
