num = list()
nump = list()
numi = list()
while True:
    x = int(input('Digite um valor: '))
    num.append(x)
    if x % 2 == 0:
        nump.append(x)
    else:
        numi.append(x)
    res = str(input('Deseja continuar? ')).strip()[0]
    if res in 'Nn':
        break
nump.sort()
numi.sort()
print(f'A lista dos valores digitados é: {num}')
print(f'A lista dos valores pares digitados é: {nump}')
print(f'A lista dos valores ímpares digitados é: {numi}')
