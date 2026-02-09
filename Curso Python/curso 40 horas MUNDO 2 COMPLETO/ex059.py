from time import sleep
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
programa = False
maior = 0
while programa == False:
    print('''\nSelecione uma opção
          [1] Somar
          [2] Multiplicar
          [3] Maior
          [4] Trocar os números
          [5] Sair do programa''')
    escolha = int(input('\nDigite sua opção: '))
    if escolha == 1:
        print('-----PENSANDO-----')
        sleep(3)
        print('\nA soma dos dois valores é ( {} )'.format(valor1 + valor2))
    elif escolha == 2:
        print('-----PENSANDO-----')
        sleep(3)
        print('A multiplicação dos valores é ( {} )'.format(valor1 * valor2))
    elif escolha == 3:
        print('-----PENSANDO-----')
        sleep(3)
        maior = valor1
        if maior < valor2:
            maior = valor2
        print('O maior valor é ( {} )'.format(maior))
    elif escolha == 4:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif escolha == 5:
        programa = True
    else:
        print('\nCOMANDO ÍNVALIDO')
print('FIM DE PROGRAMA')