from datetime import date
nascimento = int(input('Em que ano você nasceu? '))
atual = date.today().year
idade = atual - nascimento
print('O nadador tem {} anos'.format(idade))
if idade <= 9:
    print('Você se enquadra na categoria MIRIM')
elif 9 > idade <= 14:
    print('Você se enquadra na categoria INFANTIL')
elif 14 < idade <= 19:
    print('Você se enquadra na categoria JÚNIOR')
elif 19 < idade <= 25:
    print('Você se enquadra na categoria SÊNIOR')
else:
    print('Você se enquadra na categoria MASTER')
