from math import factorial  # Módulo Math
n = int(input('Digite um número para calcular seu Factorial: '))
f = factorial(n)  # Factorial
factorial = n
print(f'Calculando {n}! = {n} ', end='')
for c in range (n-1, 0, -1):
    factorial *= c
    print(f'x {c} ', end='')
print('=', factorial)
