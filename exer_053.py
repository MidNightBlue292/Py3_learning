msg = str(input('Digite uma frase: ')).strip().upper()
msg = msg.split()
junto = ''.join(msg)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')
