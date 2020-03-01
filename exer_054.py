from datetime import date
c1 = 0
c2 = 0
data = date.today().year
n = int(input('Quantas pessoas são? '))
for c in range(1,n+1):
    ano = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if data - ano >= 18:
        c1 += 1
    else:
        c2 += 1
print(f'Ao todo tivemos {c1} pessoas maiores de idade.')
print(f'E também tivemos {c2} pessoas menores de idade')
