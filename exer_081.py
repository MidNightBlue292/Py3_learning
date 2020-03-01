lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    resposta = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-' * 20)
print(f'Foram digitados {len(lista)} valores...')
print(f'Os valores da lista foram {lista}')
lista.sort()
print(f'Os valores da lista em ordem crescente {lista}')
lista.reverse()
print(f'Os valores da lista em ordem decrescente {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
