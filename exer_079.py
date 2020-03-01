lista = []
while True:
    número = int(input('Digite um valor: '))
    if número not in lista:
        print('Valor adicionado com sucesso!')
        lista.append(número)
    else:
        print('Valor duplicado. Não vou adicionar!')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'nN':
        break
lista.sort()
print(lista)
