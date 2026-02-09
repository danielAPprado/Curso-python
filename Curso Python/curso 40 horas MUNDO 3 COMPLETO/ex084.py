temp = []
pessoas = []
maior = menor = 0
while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(int(input('Digite o peso: ')))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if maior < temp[1]:
            maior = temp[1]
        if menor > temp[1]:
            menor = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    continua = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
    while continua not in 'sn':
        continua = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
    if continua == 'n':
        break
print(f'Ha {len(pessoas)} pessoas na lista, os dados foram {pessoas}')
print(f'O maior peso foi {maior}', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
