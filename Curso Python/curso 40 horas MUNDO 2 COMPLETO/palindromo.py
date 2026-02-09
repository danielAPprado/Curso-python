print('DETECTOR DE PALÍNDROMOS')
frase = str(input('\nDigite sua frase/palavra: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('=-=' * 25)
print('\nSua frase {}\nao contrario fica {}\n'.format(junto, inverso))
print('=-=' * 25)
if inverso == junto:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
print('')