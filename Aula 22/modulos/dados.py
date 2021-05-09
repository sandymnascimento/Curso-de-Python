def leiaDinheiro(txt):
    while txt.isalpha() or txt == '':
        print(f'\033[31mERRO: "{txt}" é um preço inválido.\033[m')
        txt = input('Digite o preço: R$').replace(',', '.').strip()
    return float(txt)


def leiaint(n):
    n = input('Digite um número: ').strip()
    while not n.isnumeric():
        print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        n = leiaint('Digite um número: ')
    return n