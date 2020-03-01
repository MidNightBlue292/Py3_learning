n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
total = (n1+n2)/2
# Modo 1 Old version
print('A média é: {:.1f}'.format(total))
# Modo 2 New version
print(f'A média é: {total:.1f}')
