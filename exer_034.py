salário = float(input('Qual o salário do funcionário? '))
if salário <= 1250:
    per = 15
    novo = salário + (salário * per / 100)
else:
    per = 10
    novo = salário + (salário * per / 100)
print('Com um salário de {:.2f}€ houve um aumento de {}% ficando assim a receber {:.2f}€'.format(salário, per, novo))
