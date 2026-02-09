real = float(input('Quantos reais deseja converter? R$'))
dolar = real / 5.42
euro = real / 6.34
iene = real / 0.035
print('Você pode comprar com {:.2f} reais \n {:.2f} dolares \n {:.2f} euros \n {:.2f} ienes'.format(real, dolar, euro, iene))