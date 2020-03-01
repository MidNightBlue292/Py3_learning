n = int(input('Digite um número inteiro: '))
a = n - 1
s = n + 1
# Modo 1
print('O antecessor é', n-1, 'o sucessor é', n+1)
# Modo 2 Old Version
print('O antecessor é {} o sucessor é {}'.format(a, s))
print('Analisando o número {} o antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))
# Modo 3 New Version
print(f'Analisando o número {n} o antecessor é {a} e o sucessor é {s}')
