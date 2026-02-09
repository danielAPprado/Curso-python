lista = []
for c in range(0, 5):
    n = int(input(f'Digite o valor {c}: '))
    if c == 0 or n > lista[-1]:
        print('Adicionado ao fim da lista')
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado a {pos}ª posição')
                break
        pos += 1
print(f'Os valores digitados foram {lista}')
