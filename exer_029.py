vel = int(input('Velocidade do veículo -> '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Excedeste o limite de velocidade...')
    print('Tens de pagar {}€'.format(multa))
print('Conduza com cuidado!')
