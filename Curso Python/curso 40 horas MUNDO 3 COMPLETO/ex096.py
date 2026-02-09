def area(larg, comp):
    conta = larg * comp
    print('-*-' * 20)
    print(f'A área de largura {larg} e comprimento {comp} é : {conta:.1f} m²')
    print('-*-' * 20)


l = float(input('Digite a largura (m) : '))
c = float(input('Digite o comprimento (m) : '))
area(l, c)
