def escreva(nome):
    n = len(nome) + 4
    print('~' * n)
    print(f'  {nome}  ')
    print('~' * n)

escreva(input('Nome: '))
