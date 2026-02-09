lista = []
listapar = []
listaimpar = []
while True:
    lista.append(int(input('Digite um número: ')))
    continua = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
    while continua not in 'sn':
        continua = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
    if continua == 'n':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v) 
print(f'Os valores digitados foram {lista}')
print(f'Os valores impares foram {listaimpar}')
print(f'Os valores pares foram {listapar}')