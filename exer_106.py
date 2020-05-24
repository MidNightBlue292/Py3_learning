def cores():
    c= ('\033[m',          # 0- sem cor
        '\033[0;30;41m',   # 1- vermelho
        '\033[0;30;42m',   # 2- verde
        '\033[0;30;43m',   # 3- amarelo
        '\033[0;30;44m',   # 4- azul
        '\033[0;30;45m',   # 5- roxo
        '\033[7;30'        # 6- branco
    )
    return c

def ajuda(com):
    print(c[6], end='')
    help(com)
    print(c[6], end='')

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor])
    print('~' * tam)
    print(' ', msg, ' ')
    print('~' * tam)
    print(c[0], end= '')

# Programa Principal
comando = ''
c = cores()
while True:
    título('Sistema de ajuda PyHelp', 3)
    comando = str(input('Função ou Biblioteca >> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('** Finalizando **',1)
