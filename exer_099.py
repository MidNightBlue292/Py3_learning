def maior(*num):  # *num várias entradas de valores
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    
    for valor in num:
        print(f'{valor} ', end='', flush=True)
                
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        
        cont +=1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(1, 2, 3, 4, 5, 6, 7, 8, 9)
maior(45, 5, 8 ,15)
maior(34,6 ,3234, 6)
maior(0)
print('Fim')
