dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O valor a pagar ficará em R${:.2f}'.format(pago))