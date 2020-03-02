lista = []
temp = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    lista.append(temp[:])
    temp.clear()
    resposta = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-' * 20)
print(f'Os valores da lista foram {lista}')
print(f'Foram introduzidos {len(lista)} pessoas.')
print(f'O maior peso foi de {maior:.1f}kg. Peso de',end=' ')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi de {menor:.1f}kg. Peso de',end=' ')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}',end=' ')
