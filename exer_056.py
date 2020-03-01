somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher18 = 0
n = int(input('Quantas pessoas? '))
for c in range (1, n+1):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome -> ')).strip()
    idade = int(input('Idade-> '))
    sexo = str(input('Sexo [M/F]-> ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 18:
        totmulher18 += 1
mediaidade = somaidade / n
print(f'A média de idade do grupo é de {mediaidade:.0f} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos chama-se {nomevelho}.')
print(f'Ao todo são {totmulher18} mulheres com menos de 18 anos.')
