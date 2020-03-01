while True:
    print('-'*40)
    n = int(input('Digite um número para ver sua tabuada: '))
    print('-'*40)
    if n < 0:
        break
    else:
        for c in range (1, 11):
            print('{} x {:2} = {}'.format(n, c, n*c))
print('Programa Tabuada Encerrado.\nVolte sempre!')
