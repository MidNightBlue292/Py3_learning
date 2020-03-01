sexo = str(input('Informe o seu sexo [M/F] -> ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Dados inválidos. Por favor, informe o seu sexo [M/F] -> ')).strip().upper()[0]
if sexo == 'M':
    print('Sexo Masculino registrado com sucesso.')
if sexo == 'F':
    print('Sexo Feminino registrado com sucesso.')
