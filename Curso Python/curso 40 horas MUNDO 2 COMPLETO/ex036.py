casa = float(input('Qual o valor da casa que deseja comprar?'))
salario = float(input('Qual o valor do seu salário mensal? '))
anos = int(input('Por quantos anos deseja pagar? '))
prestacao = casa / (anos * 12)
print('Para se pagar uma casa de {:.2f} reais em {} anos'.format(casa, anos))
print('A prestação será de {:.2f} reais'.format(prestacao))
if ((salario * 30) / 100) < prestacao:
   print('Pobres não possuem direitos aqui senhor')
else:
   print('O senhor podera receber o empréstimo')