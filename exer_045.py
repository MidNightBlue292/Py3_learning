from time import sleep
from random import randint
itens =('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
op = int(input('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
Qual a sua jogada? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if op == 0 and comp == 1 or op == 1 and comp == 2 or op == 2 and comp == 0:
    result = 'PERDEU'
elif op == 0 and comp == 2 or op == 1 and comp == 0 or op == 2 and comp == 1:
    result = 'GANHOU'
else:
    result = 'EMPATE'
print('=' * 20)
print(f'Jogador = {itens[op]}\nComputador = {itens[comp]}')
print('=' * 20)
print(result)
