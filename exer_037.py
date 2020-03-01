n = int(input('Digite um número -> '))
print('1-> BINÁRIO')
print('2-> OCTAL')
print('3-> HEXADECIMAL')
e = int(input('Escolha -> '))
if e == 1:
    print(f'O número {n} convertido para Binário -> {bin(n)[2:]}')
elif e == 2:
    print(f'O número {n} convertido para Octal -> {oct(n)[2:]}')
elif e == 3:
    print(f'O número {n} convertido para Hexadecimal -> {hex(n)[2:]}')
else:
    print('Comando errado...')
print('Fim')
