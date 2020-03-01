n1 = 11
n2 = 11
n3 = 11
while 1 < n1 > 10:
    n1 = float(input('Primeira nota -> '))
while 1 < n2 > 10:
    n2 = float(input('Segunda nota -> '))
while 1 < n3 > 10:
    n3 = float(input('Terceira nota -> '))
media = (n1 + n2 + n3) / 3
if media < 5.0:
    print(f'Média de {media:.1f} está REPROVADO.')
elif 7 > media >= 5.0:
    print(f'Média de {media:.1f} está em RECUPERAÇÃO.')
elif media >= 7.0:
    print(f'Média de {media:.1f} está APROVADO.')
