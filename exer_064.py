contador = soma = n = 0
n = int(input('Digite um número [999 para parar]: '))
while n!= 999: # n diferente de 999
    soma += n
    contador += 1
    n = int(input('Digite um número [999 para parar]: '))
print(f'Foram digitados {contador} números e a soma entre eles foi de {soma}.')
