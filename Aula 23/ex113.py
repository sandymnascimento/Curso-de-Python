def leiaInt():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número real válido.\033[m')
            continue
        else:
            return n


i = leiaInt()
r = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {i} e o número real foi {r}.')
