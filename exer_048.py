count = 0
soma = 0
for c in range (1, 500):
    resto = c % 2
    multi = c % 3
    if resto == 1:
        if multi == 0:
            count += 1
            soma = soma + c
print (f'A soma dos {count} números ímpares multiplos de 3 entre 1 e 500 é {soma}.')
