import moeda

p = float(input('Digite o preço: '))
taxa = float(input('Digite a taxa: '))
print(f'O dobro de {moeda.moeda(p)} é {(moeda.dobro(p, True))}')
print(f'A metade de {moeda.moeda(p)} é {(moeda.metade(p, True))}')
print(f'O preço {moeda.moeda(p)} mais {taxa}% é {(moeda.aumentar(p, taxa, True))}')
print(f'O preço {moeda.moeda(p)} menos {taxa}% é {(moeda.diminuir(p, taxa, True))}')
