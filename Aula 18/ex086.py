matriz = [[], [], []]
for c in range(0, 3):
    for i in range(0, 3):
        matriz[c].append(int(input(f'Digite o valor para a posição [{c}, {i}]: ')))
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[ {matriz[c][i]} ]', end='')
    print()
