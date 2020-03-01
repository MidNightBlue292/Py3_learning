from datetime import date
atual = date.today().year
nasc = int(input('Intruduza ano de nascimento -> '))
idade = atual - nasc
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
