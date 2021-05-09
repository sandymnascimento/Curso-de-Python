def area(a, l):
    print(f'A área de um terreno de {a}x{l} é de {a * l}m²')


print('-' * 20)
print('Controle de terrenos')
print('-' * 20)
a = float(input('ALTURA (m): '))
l = float(input('COMPRIMENTO (m): '))
area(a, l)
