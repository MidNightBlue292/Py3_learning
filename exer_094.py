pessoa = dict()
galera = list()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apénas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Por favor, digite apénas S ou N.')
    if resp == 'N':
        break

# Informação 1
print('-' * 40)
print(f'Ao todo temos {len(galera)} pessos cadastradas.')

# Informação 2
print('-' * 40)
média = 0
for m in galera:
    média += int(m['idade'])
média = média / len(galera)
print(f'A média de idade é de {média:5.2f} anos.')

# Informação 3
print('-' * 40)
print('As mulheres cadastradas foram:')
for p in galera:
    if p['sexo'] in 'F':
        print(f'  {p["nome"]}')

# Informação 4
print('-' * 40)
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()

print('-' * 40)
print('<< FIM >>')
