num = int(input('Digite um número inteiro -> '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
um = num // 1000 % 10
dm = num // 10000 % 10
cm = num // 100000 % 10
umm = num // 10000000 % 10
print('Analisando o número {}'.format(num))
print('{} Unidades'.format(u))
print('{} Dezenas'.format(d))
print('{} Centenas'.format(c))
print('{} Unidades de milhar'.format(um))
print('{} Dezenas de milhar'.format(dm))
print('{} Centenas de milhar'.format(cm))
print('{} Unidade de milhão'.format(umm))
