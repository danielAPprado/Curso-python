lista = {}
gols = []
lista['nome'] = str(input('Qual o nome do jogador? '))
partidas = int(input(f'Quantas partidas o jogador {lista["nome"]} jogou? '))
for c in range(1, partidas+1):
    gols.append(int(input(f'Quantos gols ele fez na {c}ª partida: ')))
lista['gols'] = gols[:]
lista['total'] = sum(gols)

print(f'\n{lista}')

for k, v in lista.items():
    print(f'{k} = {v}')

print(f'O jogador {lista["nome"]} jogou {len(lista["gols"])} partidas')

for i, v in enumerate(gols):
    print(f'Na partida {i+1} {lista["nome"]} fez {v} gols')

print(f'\nTotal = {lista["total"]}')