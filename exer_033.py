a = int(input('Primeiro número -> '))
b = int(input('Segundo número -> '))
c = int(input('Terceiro número -> '))
# Descobrir número menor
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Descobrir número maior
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O número {} é o menor'.format(menor))
print('O número {} é o maior'.format(maior))
