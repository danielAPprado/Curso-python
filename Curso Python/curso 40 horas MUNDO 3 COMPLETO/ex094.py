lista = []
dicionario = {}
media = soma = 0
while True:
    dicionario.clear()
    dicionario['nome'] = str(input('Nome: '))
    while True:
        dicionario['sexo'] = str(input('Sexo [M/F]: ')).lower().strip()[0]
        if dicionario['sexo'] in 'mf':
            break
        print('ERRO! APENAS M ou F')
    dicionario['idade'] = int(input('Idade: '))
    soma += dicionario['idade']
    continua = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
    lista.append(dicionario.copy())
    while continua not in 'sn':
        continua = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
    if continua == 'n':
        break
print(f'A) Ao todo temos {len(lista)} pessoas cadrastadas')
print(f'B) A média de idade é de {soma / len(lista):.2f}')
print(f'C) As mulheres cadrastadas foram ', end=' ')
for p in lista:
    if p['sexo'] == 'f':
        print(f'{p["nome"]}', end=' ')
print()
print(f'D) lista de pessoas acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('ENCERRANDO')