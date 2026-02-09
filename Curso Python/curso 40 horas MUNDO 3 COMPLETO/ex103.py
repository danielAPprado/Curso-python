def ficha(nome='desconhecido', gols=0):
    print(f'O jogador {nome} marcou {gols} gols')

n = str(input("Nome: "))
g = str(input("Quantos gols o jogador marcou? "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
