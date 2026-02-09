from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano {}ª pessoa nasceu? '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Há {} pessoas maiores de idade e {} menores de idade'.format(totmaior, totmenor))