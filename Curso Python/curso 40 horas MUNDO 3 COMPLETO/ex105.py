def notas(*n, situacao=False):
    dici = {}
    dici['total'] = len(n)
    dici['maximo'] = max(n)
    dici['minimo'] = min(n)
    dici['media'] = sum(n)/len(n)
    if situacao:
        if dici['media'] >= 7:
            dici['situação'] = 'BOA'
        elif dici['media'] >= 5:
            dici['situação'] = 'MÉDIA'
        else:
            dici['situação'] = 'RUIM'

    return dici


#Programa principal
resp = notas(5.5, 3.1, 1.7, 10, 12, situacao=True)
print(resp)