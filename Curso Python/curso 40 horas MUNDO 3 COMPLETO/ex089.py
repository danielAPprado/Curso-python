ficha = []
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a nota do aluno: '))
    nota2 = float(input('Digite a outra nota do aluno: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continua = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
    while continua not in 'sn':
        continua = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
    if continua == 'n':
        break
print('-=' * 30)
print(f'{'Nº.':<4}{'NOME':<10}{'MEDIA':>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? 999 para interromper: '))
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('Volte sempre')