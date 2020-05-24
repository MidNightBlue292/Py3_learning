from time import sleep

def contagem(i, f, p):
    print('-' * 30)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print(f'Contagem de {i} até {f} de {p} em {p}')
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)  # ", flush=True" reset time (version 3.6.9) 
            cont += p
            sleep(0.2)
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)  # ", flush=True" reset time (version 3.6.9)
            sleep(0.2)
            cont -= p
        print('Fim!')

contagem(1, 10, 1)
contagem(10, 0, 2)

print('-' * 30)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contagem(ini, fim, pas)
print('-' * 30)
