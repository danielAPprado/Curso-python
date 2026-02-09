jogador = {}
gols = []
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Qual o nome do jogador? '))
    partidas = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))
    gols.clear()
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols ele fez na {c+1}ª partida: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        continua = str(input('Quer continuar? [S/N]: ')).lower().strip()[0]
        if continua in 'sn':
            break
        print('ERRO! Apenas [S/N]')
    if continua == 'n':
        break
print(' cod ', end='')
for i in jogador.keys():
    print(f'{i:>15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
while True:
    busca = int(input('\nQuer ver os dados de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'\nErro! não existe jogador com o índice {busca}')
    else:
        print(f'\nLevantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    Na partida {i+1} marcou {g} gols.')
print('Volte sempre!')
