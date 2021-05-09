from random import randint
from time import sleep


def sorteia(lst):
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        lst.append(randint(0, 100))
        print(lst[c], end=', ')
        sleep(0.5)
    print('PRONTO!')


def somaPar(lst):
    soma = 0
    for v in lst:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores PARES de {lst}, temos {soma}.')


numeros = list()
sorteia(numeros)
somaPar(numeros)