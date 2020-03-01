from datetime import date
atual = date.today().year
nascimento = 3000
while nascimento > atual or nascimento < 1900:
    nascimento = int(input('Qual o ano de nascimento? '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}.')
if idade == 18:
    print('Tem de se alistar imediatamente!!!')
elif idade > 18:
    saldo = idade - 18
    print(f'Já deveria ter feito o alistamento á {saldo} ano(s).')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}.')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} ano(s) para se alistar.')
    ano = atual + saldo
    print(f'Seu alistamento será em {ano}')
print('FIM')
