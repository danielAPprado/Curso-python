valor = int(input('Qual valor quer sacar? '))
total = valor
ced = 50
count = 0
while True:
    if total >= ced:
        total -= ced
        count += 1
    else:
        print(f'O seu valor {valor} pode ser lhe entregue em {count} cédulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced =1
        count = 0
        if total == 0:
            break
