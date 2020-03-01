# aumento de 15%
porcentagem = 15
salário = float(input('Qual o salário do funcionário? € '))
aumento = salário + (salário * porcentagem / 100)
print(f'O salário do funcionário era {salário:.2f}€')
print(f'Se tiver um aumento de {porcentagem}%')
print(f'Ficará a receber {aumento:.2f}€')
