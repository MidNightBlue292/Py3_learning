from random import randint
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = impares = coluna = maior = 0
for l in range(0,3):
    for c in range(0, 3):
        m = randint(1, 9)
        matriz[l][c] = m
        print(f'O valor em [{l},{c}] é {m}')
print(f'{" Matriz ":-^14}')
print(f'   0   1   2')
print(f'0 {matriz[0]}')
print(f'1 {matriz[1]}')
print(f'2 {matriz[2]}')
print('-' * 14)
for l in range(0,3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        else:
            impares += matriz[l][c]
        if c == 2:
            coluna += matriz[l][c]
        if l == 1 and c == 0:
            maior = matriz[l][c]
        else:
            if maior < matriz[l][c]:
                maior = matriz[l][c]
print(f'A soma dos números pares é {pares}')
print(f'A soma dos números ímpares é {impares}')
print(f'A soma dos números da terceira coluna é {coluna}')
print(f'O maior valor da segunda linha é {maior}')
