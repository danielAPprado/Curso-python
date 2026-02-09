count = 0
num = 0
soma = 0
while num != 999:
    num = int(input('Digite um número, [999] para parar: '))
    soma += num
    count += 1
print('FIM, você digitou {} números e a soma deles é {}'.format(count - 1, soma - 999))