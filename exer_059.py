primeiro = int(input('1º valor: '))
segundo = int(input('2º valor: '))
opção = 0
while opção != 5:
    opção = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n>>>>> Qual é a sua opção? '))
    if opção == 1:
        print(f'{primeiro} + {segundo} = {primeiro + segundo}')
    elif opção == 2:
        print(f'{primeiro} x {segundo} = {primeiro * segundo}')
    elif opção == 3:
        if primeiro > segundo:
            print(f'O número {primeiro} é maior que {segundo}')
        else:
            print(f'O número {primeiro} é menor que {segundo}')
    elif opção == 4:
        primeiro = int(input('1º valor: '))
        segundo = int(input('2º valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
print('Fim')
