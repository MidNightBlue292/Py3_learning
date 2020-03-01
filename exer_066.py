contador = soma = n = 0
while True: # Loop infinito
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    soma += n
    contador += 1
print(f'Foram digitados {contador} números e a soma entre eles foi de {soma}.')
