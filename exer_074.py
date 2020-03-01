from random import randint
tupla = (randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9))
print('Os valor sorteados foram: ',end='')
for n in range (0,5):
    print(f'{tupla[n]}', end=' ')
print(f'\nO menor valor sorteado é o {min(tupla)}')
print(f'O maior valor sorteado é o {max(tupla)}')
