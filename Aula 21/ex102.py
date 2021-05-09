def fatorial(x, show=False):
    """
        =>Calcula o Fatorial de um número.
    :param x: O número a ser calculado.
    :param show: (Opcional) Define se o calculo será ou não exibido.
    :return: O resultado do fatorial de um número x.
    """
    f = 1
    for c in range(x, 0, -1):
        if show:
            if c != 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} =', end=' ')
        f *= c
    return f


num = int(input('Deseja o fatorial de qual valor? '))
r = input('Deseja ver o processo de cálculo? ').lower()[0]
if r in 's':
    print(fatorial(num, True))
else:
    print(fatorial(num, False))