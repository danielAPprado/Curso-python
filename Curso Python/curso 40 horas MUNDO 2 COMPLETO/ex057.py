sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, por favor insira [M/F]: ')).strip().upper()[0]
print('Seus dados foram atualizados como {} com sucesso'.format(sexo))
   