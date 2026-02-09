lista = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)    
    else:
        print('O valor não pode ser duplicado')
    continua = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
    if continua not in 'sn':
        continua = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
    if continua == 'n':
       break
lista.sort()
print(lista)