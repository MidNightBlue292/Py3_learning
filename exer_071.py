print('Banco Santander Totta')
# €uro 5/10/20/50/100/200/500
valor = int(input('Qual o valor para retirar -> €'))
total = valor
céd = 500
totcéd = 0
while True:
    if valor % 5 != 0:
        print('Valor inválido!')
        print('Só estão disponíveis notas de 500€, 200€, 100€, 50€, 20€, 10€ e 5€.')
        break
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} notas de {céd}€')
        if céd == 500:
            céd = 200
        elif céd == 200:
            céd = 100
        elif céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        totcéd = 0
        if total == 0:
            break
