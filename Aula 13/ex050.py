soma = 0
cont = 0
for c in range(1, 7):
    x = int(input(f'Digite o {c} valor: '))
    if x % 2 == 0:
        soma += x
        cont += 1
print(f'Foram digitados {cont} números pares, a soma deles é {soma}.')
