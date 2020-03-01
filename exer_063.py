cont = 3
t1 = 0
t2 = 1
print('-'*41)
print('S e q u ê n c i a  d e  F i b o n a c c i')
print('-'*41)
fibonacci = int(input('Quantos termos quer mostrar? '))
print('~'*41)
print(f'{t1} -> {t2}', end='')
while cont <= fibonacci:
    cont += 1
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
print(' -> FIM')
print('~'*41)
