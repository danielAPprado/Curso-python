print('GERADOR DE P.A')
primeiro = int(input('Qual o primeiro termo da P.A: '))
razao = int(input('Qual a razão da P.A: '))
termo = primeiro
count = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while count <= total:
        print('{} '.format(termo), end='')
        termo += razao
        count += 1
    print('PAUSA')
    mais = int(input('Você quer quantos mais termos? '))
print('Progressão finalizada com {} termos'.format(total))
