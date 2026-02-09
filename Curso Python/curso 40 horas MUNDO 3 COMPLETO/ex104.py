def leiaInt(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! digite apenas um número inteiro')
        if ok:
            break
    return(valor)

#Programa principal
n = leiaInt('Digite um número e apenas um número ')
print(f'Você digitou o número {n}')