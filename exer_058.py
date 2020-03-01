from random import randint
t = 0
c = randint(0,10)
acertou = False
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
while not acertou:
    n = int(input('Qual o seu palpite? '))
    t += 1
    if n == c:
        acertou = True
    else:
        if n > c:
            print('Menos... Tente mais uma vez.')
        elif n < c:
            print('Mais... Tente mais uma vez.')
print(f'Acertou com {t} tentativas. Parabéns!')
