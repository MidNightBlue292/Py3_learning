lista = [[],[]]
valor = 0
for c in range (1,8):
    valor = int(input(f'{c}º valor -> '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('-' * 20)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados são: {lista[0]}')
print(f'Os valores ímpares digitados são: {lista[1]}')
