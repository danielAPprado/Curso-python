count = homem = mulher = 0
while True:
    idade = int(input('Qual sua idade? : '))
    sexo = str(input('Qual seu sexo? [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo? [M/F]: ')).upper().strip()[0]
    continua = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if idade >= 18:
        count += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    if continua == 'N':
        break   
print(f'{count} pessoas tem mais de dezoito anos. Há {homem} homens na lista e {mulher} mulheres com menos de 20 anos')