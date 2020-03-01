extenso = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze',
           'Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    n = int(input('Digite um número entre (0-20) -> '))
    if 0 <= n <= 20:
        break
    print('Número inválido. Tente Novamente...')
print(f'O número digitado foi {extenso[n]}')
