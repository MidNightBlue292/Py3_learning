# triângulo retângulo = cateto oposto + cateto adjacente + hipotenusa
import math
co = float(input('Comprimento do cateto oposto -> '))
ca = float(input('Comprimento do cateto adjacente -> '))
# Modo 2
hi = (co ** 2 + ca ** 2) ** (1/2)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))
# Modo 2
hi1 = math.hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}'.format(hi1))
