print('{:=^40}'.format(' BLACK FRIDAY '))
print(' ')
valor = float(input('Qual o valor? € '))
print(' ')
print('''1- em dinheiro ou cheque
2- no cartão
3- em 2x no cartão
4- em 3x ou mais no cartão
5- terminar''')
op = int(input('Opção -> '))
if op == 1:
    total = valor - (valor * 10 / 100)
    print(f'Em dinheiro ou cheque o valor de {valor:.2f}€ fica por {total:.2f}€ com 10% desconto.')
elif op == 2:
    total = valor - (valor * 5 / 100)
    print(f'No cartão o valor de {valor:.2f}€ fica por {total:.2f}€ com 5% desconto.')
elif op == 3:
    total = valor / 2
    print(f'Em 2x no cartão o valor de {valor}€ fica por {total}€ com 0% juros.')
elif op == 4:
    parcelas = int(input('Quantas vezes? '))
    total = (valor + (valor * 20 / 100)) / parcelas
    print(f'Em {parcelas:.0f}x no cartão o valor de {valor}€ fica por {total}€ com 20% juros.')
else:
    print('Fim...')
