num = list()
while True:
    num.append(int(input('Digite um valor: ')))
    res = str(input('Deseja continuar? ')).strip()[0]
    if res in 'Nn':
        break
print(f'Foram digitados {len(num)} números.')
num.sort(reverse=True)
print(f'A lista de valores, ordenada de forma decrescente é {num}')
if 5 in num:
    print('O número 5 foi digitado e está contido na lista.')
else:
    print('O número 5 não foi digitado, portanto não aparece na lista.')