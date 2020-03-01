pares = 0
ímpares = 0
for c in range (1, 7):
    num = int(input(f'Digite {c}º número -> '))
    if num % 2 == 0:
        pares += num
    else:
        ímpares += num
print(f'A soma dos números pares é {pares}')
print(f'A soma dos números ímpares é {ímpares}')
