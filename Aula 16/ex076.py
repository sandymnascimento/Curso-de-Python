prod = ('Lápis', 1, 'Caneta', 1.20, 'Borracha', 2.50, 'Caderno', 15.90, 'Estojo', 25.00, 'Kit de réguas', 8.90, 'Kit canetas coloridas', 27.50,
        'Planner anual', 35.80, 'Mochila', 145.00, 'Compasso', 9.99)
print("=" * 44)
print(' ' * 11, 'LISTAGEM DE PREÇOS')
print('=' * 44)

for c in range(0, len(prod)):
    if c % 2 == 0:
        print(f'{prod[c]:.<35}R$', end='')
    else:
        print(f'{prod[c]:>7.2f}')