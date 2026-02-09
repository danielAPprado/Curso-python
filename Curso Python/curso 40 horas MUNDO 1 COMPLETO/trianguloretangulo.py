#n1 = float(input('Digite um cateto: '))
#n2 = float(input('Digite outro cateto: '))
#h = (n1 ** 2 + n2 ** 2) **(1/2) 
#print('A soma do cateto 1 ({:.2f}) com o cateto 2 ({:.2f}) resulta na hipotenusa {:.2f}'.format(n1, n2, h))

import math
n1 = float(input('Digite um cateto: '))
n2 = float(input('Digite outro cateto: '))
h = math.hypot(n1, n2)
print('A soma do cateto 1 ({:.2f}) com o cateto 2 ({:.2f}) resulta na hipotenusa {:.2f}'.format(n1, n2, h))
