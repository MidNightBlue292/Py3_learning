print('10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
primeiro = int(input('Primeiro termo -> '))
razão = int(input('Razão -> '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razão
    cont += 1
print('FIM')
