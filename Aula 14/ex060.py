x = int(input('Digite um número para calcular o seu fatorial: '))
fat = x
print(f'Calculando {x}! =', end=' ')
while x != 1:
    print(f'{x} x', end=' ')
    fat = fat * (x - 1)
    x -= 1
print(f'1 = {fat}')