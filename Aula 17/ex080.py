num = list()
for c in range(0, 5):
    x = int(input('Digite um valor: '))
    if c == 0 or x > num[-1]:
        num.append(x)
        print('Adicionado ao final da lista.')
    else:
        for i in range(0, len(num)):
            if x <= num[i]:
                print(f'Adicionado na posição {i} da lista.')
                num.insert(i, x)
                break
print(f'Ordenei a lista dos valores digitados, observe: {num}')
