from random import randint
from time import sleep
numero = [0, 0, 0, 0, 0]
estrela = [0,0]
print('-' * 40)
print(f'{" E U R O M I L H Õ E S ":^40}')
print('-' * 40)

for n in range (0,5):
    while True:
        num = randint(1, 50)
        if num not in numero:
            numero[n] = num
            break
for n in range (0,2):
    while True:
        num = randint(1, 12)
        if num not in estrela:
            estrela[n] = num
            break
numero.sort()
estrela.sort()
print(f'Números  -> {numero}')
print(f'Estrelas -> {estrela}')
print('-' * 40)
