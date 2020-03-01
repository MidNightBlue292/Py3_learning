n = int(input('Digite um número: '))
# Modo 1
print('O dobro de {} é {}'.format(n, (n*2)))
print('O triplo de {} é {}'.format(n, (n*3)))
print('A raiz quadrada de {} é {:.2f}'.format(n, (n**(1/2))))
# Modo 2
print(f'O dobro de {n} é {n*2}')
print(f'O triplo de {n} é {n*3}')
print(f'A raiz quadrada de {n} é {n**(1/2):.2f}')
