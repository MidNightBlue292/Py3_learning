n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
t = n1 + n2
# Modo 1 Old version
print('A soma entre {} e {} é {}'.format(n1, n2, t))
print('O total da soma é: {}'.format(t))
# Modo 2
print('A soma entre', n1, 'e', n2, 'é', t)
print('O total da soma é:', n1+n2)
# Modo 3 New version
print(f'A soma entre {n1} e {n2} é {t}')
print(f'O total da soma é: {t}')
