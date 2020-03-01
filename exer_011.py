largura = float(input('Largura da parede (metros)? '))
altura = float(input('Altura da parede (metros)? '))
area = largura*altura
litro = area/2
print('A sua parede tem a dimensão de {:.2f}m x {:.2f}m e sua área é de {:.2f}m2.'.format(largura, altura, area))
print('Para pintar essa parede vais precisar de {:.2f} litros de tinta.'.format(litro))
