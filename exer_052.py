count = 0
num = int(input('Digite um número inteiro -> '))
for c in range(1,num+1):
    if num % c == 0:
        count += 1
        print(f'\033[0;32m{c}\033[m', end=' ')
    else:
        print(f'\033[0;31m{c}\033[m', end=' ')
print(f'\nO número {num} foi divisível {count} vezes.')
if count == 2:
    print('Ele é um número primo!')
else:
    print('Ele não é um número primo!')
