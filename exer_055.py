phi = 0
plo = 0
for n in range (1,6):
    peso = float(input(f'Peso da {n}ª pessoa: '))
    if n == 1:
        phi = peso
        plo = peso
    else:
        if peso > phi:
            phi = peso
        if peso < plo:
            plo = peso
print(f'O maior peso lido foi de {phi:.1f}Kg')
print(f'O menor peso lido foi de {plo:.1f}Kg')
