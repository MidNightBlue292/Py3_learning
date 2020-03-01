print('10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
termo = int(input('Primeiro termo -> '))
razão = int(input('Razão -> '))
décimo = termo + (10-1) * razão # Fórmula
for c in range (termo, décimo + razão, razão):
    print(c, end=" -> ")
print('Fim', end='')
