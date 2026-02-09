import random
num = random.randint(1, 5)
print('-=-' * 30)
print('O computador pensará num numero de um a cinco! Tente adivinhar qual numero ele pensou!')
print('-=-' * 30)
resposta = int(input('Qual número você acha que foi escolhido? : '))
if resposta == num:
    print('Parabéns! Você acertou! era o numero {}! '.format(num))
else:
    print('Perdão, parece que você errou! O número era {}! '.format(num))