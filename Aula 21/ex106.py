c = ('\033[m', '\033[1;32m', '\33[1;42m', '\033[34m', '\33[31m', '\033[47m')


def ajuda(txt):
    from time import sleep
    sleep(0.3)
    print(c[4] + f'Acessando o manual do comando: \'{txt}\'.' + c[0])
    sleep(0.3)
    print(c[5])
    help(txt)
    print(c[0], end='')
    sleep(1)


while True:
    print(c[1] + '~' * 25 + c[0])
    print(c[2] + ' SISTEMA DE AJUDA PyHELP ' + c[0])
    print(c[1] + '~' * 25 + c[0])
    txt = input('Função ou biblioteca: ').lower()
    if txt in 'fim':
        print(c[3] + 'PROGRAMA ENCERRADO!')
        break
    ajuda(txt)