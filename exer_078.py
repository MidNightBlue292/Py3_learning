lista = []
for n in range (0,5):
    lista.append(int(input(f'Digite um valor para a posição {n} -> ')))
print('-='*20)
print(f'Os valores são {lista}')
maior = max(lista)
menor = min(lista)
print(f'O maior número é {maior} aparece na posição ',end='')
for indice, valor in enumerate(lista):
    if valor == maior:
        print(f'{indice}',end='..')
print(f'\nO menor número é {menor} aparece na posição ',end='')
for indice, valor in enumerate(lista):
    if valor == menor:
        print(f'{indice}',end='..')
print('\nAcabou...')
