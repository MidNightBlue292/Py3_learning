# Bissexto ocorre a cada 4 anos (excepto anos múltiplos de 100 que não são múltiplos de 400)
from datetime import date
ano = int(input('Digite um ano ou 0 para atual-> '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!!!'.format(ano))
else:
    print('O ano {} não é BISSEXTO!!!'.format(ano))
