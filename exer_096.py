def area(l, c):
    return l * c

print('Controle de Terrenos')
print('-------- -- --------')
print()
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
a = area(l, c)
print()
print(f'A área de um terreno de {l}m x {c}m é de {a}m²')
