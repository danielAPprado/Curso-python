from time import sleep


def contagem(i, f, p):
    print(f'contagem de {i} até {f} de {p} em {p}')
    if i < f:
        count = i
        while count <= f:
            print(f'{count} ', end='', flush=True)
            sleep(0.3)
            count += p
        print('FIM')
    else:
        count = i
        while count >= f:
            print(f'{count} ', end='', flush=True)
            sleep(0.3)
            count -= p
        print('FIM')


contagem(1, 10, 1)
contagem(10, 0, 2)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)
