tupla = (int(input('1º número -> ')), int(input('2º número -> ')),
         int(input('3º número -> ')), int(input('4º número -> ')))
print(f'Os valores foram : {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)}x')
if 3 in tupla:
    print(f'O número 3 aparece pela 1ª vez na {tupla.index(3)+1} posição')
else:
    print('O número 3 não foi digitado')
print('Os números pares digitados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(f'{n}',end=' ')
