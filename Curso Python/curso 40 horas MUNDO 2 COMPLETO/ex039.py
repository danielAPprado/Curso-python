from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} anos no ano {}'.format(ano, idade, atual))
menor = 18 - idade
maior = idade - 18
if idade == 18:
    print('Você deve se alistar imediatamente!')
elif idade < 18:
    print('Você deverá se alistar em {} anos, em {}'.format(menor, menor + atual))
elif idade > 18:
    print('Você deveria ter se alistado em {} a {} anos atras'.format(atual - maior, maior))
else:
    print('Algo deu errado')
