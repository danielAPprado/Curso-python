count = num = soma = maior = menor = 0
resposta = 'S'
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    count += 1
    if count == 1:
        maior = menor = num
    if maior < num:
        maior = num
    if menor > num:
        menor = num
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
media = soma / count
print('\nFIM, você digitou {} números e a soma deles é {}'.format(count, soma))
print('O maior número é {} e o menor é {} e a média é {}'.format(maior, menor, media))