print('-=-' * 15)
print('Conversor Binário / Octadecimal / Hexadecimal')
print('-=-' * 15)
num = int(input('Digite o número a ser convertido: '))
num1 = int(input('Digite 1 para converter para Binário. 2 para converter para Octal. E 3 para converter para Hexa '))
if num1 == 1:
    print(bin(num)[2:])
elif num1 == 2:
    print(oct(num)[2:])
elif num1 == 3:
    print(hex(num)[2:])
else:
    print('Opção inválida, apenas são aceitos 1, 2 e 3 como resposta senhor/a')
