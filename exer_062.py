print('10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
primeiro = int(input('Primeiro termo -> '))
razão = int(input('Razão -> '))
termo = primeiro
cont = 1
pa = 10
while cont <= pa:
    print(f'{termo} -> ', end='')
    termo += razão
    cont += 1
    if cont == pa + 1:
        print('PAUSA')
        maistermos = int(input('Quantos termos vc quer mostrar mais? '))
        pa += maistermos
print(f'Progressão finalizada com {pa} termos mostrados.')
