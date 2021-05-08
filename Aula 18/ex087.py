matriz = [[], [], []]
pares = soma = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[c].append(int(input(f'Digite o valor para a posição [{l}, {c}]: ')))
        if matriz[l][c] % 2 == 0: pares += matriz[l][c]
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[ {matriz[c][i]} ]', end='')
        if c == 1 and i == 0:
            maior = matriz[c][i]
        elif c == 1 and matriz[c][i] > maior:
            maior = matriz[c][i]
        if i == 2:
            soma += matriz[c][i]
    print()
print(f'A soma dos números pares é igual a {pares}.')
print(f'A soma dos valores da terceira coluna é igual a {soma}.')
print(f'O maior valor da segunda linha é {maior}.')
