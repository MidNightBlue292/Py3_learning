c = 0
op = ''
média = 0
maior = 0
menor = 0
while op in 'Ss':
    n = int(input('Digite um número -> '))
    if c == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    c += 1
    média += n
    op = str(input('Quer continuar? [S/N] '))
média = média / c
print(f'Foram digitados {c} números e a média foi {média:.1f}\nO maior valor foi {maior} e o menor foi {menor}')
