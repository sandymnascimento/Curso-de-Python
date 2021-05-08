soma = cont = 0
while True:
    x = int(input('Digite um número: [999 para PARAR] '))
    if x == 999:
        break
    else:
        cont += 1
        soma += x
print(f'Foram digitados {cont} números e a soma entre eles é {soma}.')