cont_mais_18 = cont_fem_inf_18 = cont_masc = 0
while True:
    print('-'*40)
    print(f'{"Cadastre uma pessoa":^40}')
    print('-'*40)
    idade = int(input('Idade -> '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F] -> ')).strip().upper()[0]
    if idade >= 18:
        cont_mais_18 += 1
    if sexo == 'M':
        cont_masc +=1
    if sexo == 'F' and idade < 18:
        cont_fem_inf_18 += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar [S/N] -> ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont_mais_18}')
print(f'Ao todo temos {cont_masc} homem(s) cadastrados.')
print(f'Temos {cont_fem_inf_18} mulher(es) com menos de 18 anos.')
