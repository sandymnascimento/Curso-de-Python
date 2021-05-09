def aumentar(p, x, f=False):
    res = p + (x/100) * p
    return res if f is False else moeda(res)


def diminuir(p, x, f=False):
    res = p - (x/100) * p
    return res if f is False else moeda(res)


def dobro(p, f=False):
    if f:
        return moeda(p * 2)
    else:
        return p * 2


def metade(p, f=False):
    if f:
        return moeda(p / 2)
    else:
        return p / 2


def moeda(p):
    return f'R${p:.2f}'.replace('.', ',')


def resumo(p, aum, red):
    print('-' * 35)
    print(f'{"RESUMO DO VALOR":>25}')
    print(f'{"Metade do preço:":<25}{metade(p, True):>10}')
    print(f'{aum}{"% de aumento:":<23}{aumentar(p, aum, True):>10}')
    print(f'{red}{"% de desconto:":<23}{diminuir(p, red, True):>10}')
    print('-' * 35)