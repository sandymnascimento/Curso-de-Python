def leiaint(n):
    n = input('Digite um número: ').strip()
    while not n.isnumeric():
        print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        n = leiaint('Digite um número: ')
    return n


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}.')