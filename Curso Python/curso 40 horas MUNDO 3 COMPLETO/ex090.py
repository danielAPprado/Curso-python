aluno = {}
aluno['nome'] = str(input('Qual o nome do aluno? '))
aluno['média'] = float(input('Qual a média do aluno? '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] > 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} = {v}')
