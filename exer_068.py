from random import randint
contador = 0
print('=-'*14)
print('Vamos jogar Par ou Ímpar!')
print('=-'*14)
while True:
    jogador = int(input('Digite um valor -> '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
    print(f'Jogador {jogador} - Computador {computador} - Total {total} - ', end='')
    print('Deu Par' if total % 2 == 0 else 'Deu Ímpar')  # Expressão condicional (operação ternária)
    if tipo == 'P':
        if total % 2 == 0:
            print('Ganhaste!')
            contador += 1
        else:
            print('Perdeste!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Ganhaste!')
            contador += 1
        else:
            print('Perdeste!')
            break
    print('=-' * 14)
    print('Vamos jogar novamente...')
    print('=-' * 14)
print(f'Acabou o jogo!!! Ganhaste {contador}x')
