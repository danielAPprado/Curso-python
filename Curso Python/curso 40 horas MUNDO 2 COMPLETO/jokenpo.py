from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opcao = int(input('Digite sua escolha: '))
print('JÔ')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('=-='*12)
print('O jogador jogou {}'.format(itens[opcao]))
print('O computador escolheu {}'.format(itens[computador]))
print('=-='*12)
if computador == 0: #c joga pedra
    if opcao == 0:
        print('EMPATE')
    elif opcao == 1:
        print('VENCEU')
    elif opcao == 2:
        print('PERDEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: #c joga papel
    if opcao == 0:
        print('PERDEU')
    elif opcao == 1:
        print('EMPATE')
    elif opcao == 2:
        print('VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: #c jofa tesoura
    if opcao == 0:
        print('VENCEU')
    elif opcao == 1:
        print('PERDEU')
    elif opcao == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
