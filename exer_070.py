cont = total = quant1000 = valor = 0
produto = ' '
print('*'*40)
print(f'{"Supermercado Baratuxo":^40}')
print('*'*40)
while True:
    nome = str(input('Nome do produto -> '))
    preço = float(input('Preço -> €'))
    total += preço
    cont += 1
    if preço > 1000:
        quant1000 += 1
    if cont == 1 or preço < valor:
        produto = nome
        valor = preço
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if opção == 'N':
        break
print(f'{" Fim do programa ":-^40}')
print(f'Total -> {total}€')
print(f'Têm {quant1000} produto a custar mais de 1000€.')
print(f'O produto mais barato foi (a/o) {produto} que custa {valor:.2f}€')
