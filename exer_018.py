from math import radians, sin, cos, tan
ângulo = float(input('Digite um ângulo -> '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(ângulo, seno))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
print('O ângulo de {:.2f} tem o TANGENTE de {:.2f}'.format(ângulo, tangente))
