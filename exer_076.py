tupla = ('Lápis', 0.2,
         'Borracha', 1,
         'Caneta BIC', 0.8,
         'Marcadores 12un', 3.5,
         'Caderno linhas', 1.2,
         'Caderno liso', 1,
         'Mochila Spider Man', 15.60,
         'Livro Matemática', 5.8)
print('-'*40)
print(f'{" Listagem de Material Escolar ":-^40}')
print('-'*40)
for pos in range (0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<33}',end=' ')
    else:
        print(f'{tupla[pos]:>5.2f}€')
print('-'*40)
