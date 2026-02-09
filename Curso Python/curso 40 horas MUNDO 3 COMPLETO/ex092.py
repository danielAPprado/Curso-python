from datetime import date
lista = {}
atual = date.today().year
lista['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
carteira = int(input('Carteira de trabalho. [0] se não possuir: '))
lista['idade'] = atual - ano
if carteira != 0:
    lista['contratação'] = int(input('Qual seu ano de contratação: '))
    lista['salário'] = int(input('Qual seu salário: '))
    lista['aposentadoria'] = lista['idade'] + ((lista['contratação'] + 35) - atual)
for k, v in lista.items():
    print(f'  {k} = {v}')
