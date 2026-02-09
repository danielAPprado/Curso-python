def fatorial(n, show=False):
    '''
    Docstring for fatorial()
    -> Realiza fatoriais
    :param n: Número a receber fatorial, será destrinchado
    :param show: Decide se mostrará o resultado no fim (show=True)
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c   
    return(f)


num = int(input('Digite o número ao qual deseja a fatorial: '))
print(fatorial(num, show=True))