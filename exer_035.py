r1=float(input('Segmento de recta 1 -> '))
r2=float(input('Segmento de recta 2 -> '))
r3=float(input('Segemnto de recta 3 -> '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos de recta podem formar um triângulo')
else:
    print('Os segmentos de recta não podem formar um triângulo')
