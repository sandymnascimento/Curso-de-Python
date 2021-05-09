def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite uma opção válida.\033[m')
            continue
        else:
            return n


def linhas(tam=42):
    return "-" * tam


def titulo(msg):
    print(linhas())
    print(msg.center(42))
    print(linhas())


def menu(lista=0):
    titulo('MENU PRINCIPAL')
    for p, c in enumerate(lista):
        print(f'\033[1;33m{p + 1} - \033[m{c}')
    print(linhas())
    return leiaInt('\033[1;32mDigite a opção desejada: \033[m')
