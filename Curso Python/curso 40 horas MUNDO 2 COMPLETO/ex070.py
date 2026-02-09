soma = countp = nomeb = barato = 0
while True:
    nome = str(input('O que você comprou? '))
    preço = float(input('Qual foi o preço? '))
    continua = str(input('Quer continuar? [S/N]' )).strip().upper()
    while continua not in 'SN':
       continua = str(input('Quer continuar? [S/N]' )).strip().upper() 
    if preço > 1000:
        countp += 1
    soma += preço
    if countp == 0 or preço < barato:
        barato = preço
        nomeb = nome
    if continua == 'N':
        break
print(f'O total gasto foi de {soma:.2f}, {countp} produtos foram mais caros que R$1000 e o produto mais barato foi {nomeb}')