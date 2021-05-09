soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'A soma dos {cont} números ímpares que são multiplos de três e que se encontram no intervalo de 1 até 500 é: {soma}.')