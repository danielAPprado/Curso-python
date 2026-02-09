lista = []
count = 0
while True:
    n = int(input('Digite um número: '))
    count += 1
    lista.append(n)
    lista.sort(reverse=True)
    continua = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
    while continua not in 'sn':
        continua = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
    if continua == 'n':
        break
print(f'Sua lista foi {lista} e {count} números foram digitados') 
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')