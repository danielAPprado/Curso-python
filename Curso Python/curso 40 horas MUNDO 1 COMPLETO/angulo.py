import math
angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o seu SENO {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o seu COSSENO {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a sua TANGENTE {:.2f}'.format(angulo, tangente))
