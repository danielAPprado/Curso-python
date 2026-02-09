print('-=-' * 15)
print('ANALISADOR DE TRIÂNGULOS ')
print('-=-' * 15)
n1 = int(input('Insira o primeiro comprimento de reta: '))
n2 = int(input('Insira o segundo comprimento de reta: '))
n3 = int(input('Insira o terceiro comprimento de reta: '))
if n1 < n2 + n3 and n1 < n3 + n2 and n2 < n3 + n1:
    print('Você pode formar um triângulo com tais segmentos de reta')
    if n1 == n2 and n2 == n3:
        print('Você pode formar um triângulo EQUILÁTERO')
    elif n1 != n2 or n2 != n3 or n1 != n3:
        print('Você pode formar um triângulo ESCALENO')
    else:
        print('Você pode formar um triângulo ISÓCELES')
else:
    print('Você não pode formar um triângulo com tais segmentos de reta')