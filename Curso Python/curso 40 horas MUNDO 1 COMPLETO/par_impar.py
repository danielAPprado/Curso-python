num = int(input('Digite um número para se descobrir se ele é par ou impar '))
resultado = num % 2
if resultado == 1:
    print('O seu número é ÍMPAR')
else:
    print('O seu número é PAR')