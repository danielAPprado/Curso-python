import random
#a = str(input('Digite um nome: '))
#b = str(input('Digite um nome: '))
#c = str(input('Digite um nome: '))
#d = str(input('Digite um nome: '))
#lista = [a, b, c, d]
#escolhido = random.choice(lista)
#print('O aluno sorteado foi {}'.format(escolhido))

a = str(input('Digite um nome: '))
b = str(input('Digite um nome: '))
c = str(input('Digite um nome: '))
d = str(input('Digite um nome: '))
lista = [a, b, c, d]
random.shuffle(lista)
print(lista)