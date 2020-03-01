lista = []
listapar = []
listaimpar = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    resposta = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-' * 20)
print(f'Os valores da lista foram {lista}')
for i, v in enumerate(lista):
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)
print(f'Lista Par -> {listapar}')
print(f'Lista Ímpar -> {listaimpar}')
