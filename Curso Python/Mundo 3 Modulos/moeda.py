def dobro(n=0, form=False):
    res = n * 2
    return res if form is False else moeda(res)

def metade(n=0, form=False):
    res = n / 2
    return res if form is False else moeda(res)

def aumentar(n=0, taxa=0, form=False):
    res = n + (n * taxa/100)
    return res if form is False else moeda(res)

def diminuir(n=0, taxa=0, form=False):
    res = n - (n * taxa/100)
    return res if form is False else moeda(res)

def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')

def resumo(preco=0, aume=10, redu=5):
    print('~' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('~' * 30)
    print()
    print(f'Preço analisado:    {moeda(preco)}')
    print(f'Dobro do Preço:     {dobro(preco, True)}')
    print(f'Metade do Preço:    {metade(preco, True)}')
    print(f'{aume}% de aumento:     {aumentar(preco, aume, True)}')
    print(f'{redu}% de redução:     {diminuir(preco, redu, True)}')
    print('~' * 30)