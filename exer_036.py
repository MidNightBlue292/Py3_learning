print('EMPRÉSTIMO BANCÁRIO')
print('Compra de Habitação')
vcasa = float(input('Qual o valor da casa? € '))
salario = float(input('Qual o salário mensal? € '))
anos = float(input('Em quantos anos vai pagar? '))
pmensal = vcasa / (anos * 12)
smensal = salario - (salario * 30 / 100)
if pmensal > smensal:
    print('Empréstimo NEGADO')
    print('Para um empréstimo de {:.0f}€ em {:.0f} anos'.format(vcasa, anos))
    print('Precisa de ter um salário superior a {:.0f}€'.format(salario))
else:
    print('Empréstimo CONCEDIDO')
