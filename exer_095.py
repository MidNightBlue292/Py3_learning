jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range (0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Por favor, digite apénas S ou N.')
    if resp == 'N':
        break

print('-' * 50)
print(time)
print('-' * 50)

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print()

print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador (999 Stop)? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro: Não existe jogador com o código {busca}!')
    else:
        print(f'-- Levantamento do Jogador {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')

print('-' * 40)
print('<< Volte Sempre >>')
