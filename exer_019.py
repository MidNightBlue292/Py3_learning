from random import choice
n1 = str(input('Digite um nome -> '))
n2 = str(input('Digite um nome -> '))
n3 = str(input('Digite um nome -> '))
n4 = str(input('Digite um nome -> '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O escolhido foi o(a) -> {}'.format(escolhido))
