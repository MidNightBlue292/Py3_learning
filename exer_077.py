tupla = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS',
         'ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
for pos in tupla:
    print(f'\nNa palavra {pos} temos estas vogais ',end= '')
    for letra in pos:
        if letra in 'AEIOU':
            print(letra, end= ' ')
