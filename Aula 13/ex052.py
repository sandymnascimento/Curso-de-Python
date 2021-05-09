print('\033[1;33m=' * 30)
print('Descubra se um número é primo!')
print('=' * 30)
x = int(input('\033[mDigite o número: '))
cont = 0
for c in range(1, x + 1):
    if x % c == 0:
        cont += 1
print(f'O número foi divisível {cont} vezes.', end=' ')
if cont == 2:
    print(f'\033[1m{x} É um número primo!')
else:
    print(f'\033[1m{x} NÃO é um número primo!')