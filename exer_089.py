lista = []
while True:
    nome = str(input('Nome -> ')).strip()
    nota1 = float(input('1ª nota -> '))
    nota2 = float(input('2ª nota -> '))
    media = (nota1+nota2)/2
    lista.append([nome,[nota1,nota2],media])
    resposta = str(input('Quer continuar? [S/N] ')).strip()
    if resposta == 'Nn':
        break
print('-' * 20)
print(f'{"No.":<4}{"Nome":<10}{"Média":>6}')
print('-' * 20)
for i, v in enumerate(lista):
    print(f'{i:<4}{v[0]:<10}{v[2]:>6.1f}')
print('-' * 20)
while True:
    resposta = int(input('No. do aluno para ver as notas (999 p/sair) -> '))
    if resposta == 999:
        break
    if resposta <= len(lista)-1:
        print(f'As notas do {lista[resposta][0]} são {lista[resposta][1]} ')
print('Fim do programa!')
