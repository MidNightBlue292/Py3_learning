# km=0.15 // dias=60
km = float(input('Quantos km percorreu? '))
dias = int(input('Quantos dias usou? '))
tkm = km * 0.15
tdias = dias * 60
total = (km * 0.15) + (dias * 60)
print(f'O valor a pagar por km é {tkm:.2f}€\nO valor a pagar por dia é {tdias:.2f}€\nO total é {total:.2f}€')
