from random import randint
from time import sleep
comp = randint(0, 5)  # Faz o computador escolher um número entre 0-5
print('»' * 50)
print('Vou pensar num número entre 0-5 tenta adivinhar...')
print('«' * 50)
jogador = int(input('Em que número eu pensei??? '))
print('PROCESSANDO...')
sleep(1)
if comp == jogador:
    print('PARABÉNS...')
else:
    print('NÃO ACERTOU... eu pensei em {} e voçe em {}'.format(comp, jogador))
