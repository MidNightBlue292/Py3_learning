from random import randint
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0, 3):
        m = randint(1, 99)
        matriz[l][c] = m
        print(f'O valor em [{l},{c}] é {m}')

print(f'{" Matriz ":-^14}')
print(f'   0   1   2')
print(f'0 {matriz[0]}')
print(f'1 {matriz[1]}')
print(f'2 {matriz[2]}')
print('-' * 14)
