palavras = ('palavra', 'avada', 'kedavra', 'e', 'uma', 'maldicao', 'imperdoavel', 'de', 'harry', 'poter')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
