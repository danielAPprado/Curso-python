count = 0
soma = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    count += 1
print(f'Você digitou {count} números e a soma deles é {soma}')