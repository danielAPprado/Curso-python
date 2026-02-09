numero = (int(input('Escreva um número: ')),
          int(input('Escreva um número: ')),
          int(input('Escreva um número: ')),
          int(input('Escreva um número: ')))
print(numero)
print(f'Há {numero.count(9)} numeros 9')
if 3 in numero:
    print(f'O primeiro tres está na posição {numero.index(3)+1}')
else:
    print('O número 3 não foi digitado em posição alguma')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')