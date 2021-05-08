soma = contP = cont = p = 0
mbarato = ''
while True:
    print('\033[1m=' * 25)
    print(' ' * 8, 'PY STORE')
    print('\033[1m=\033[m' * 25)
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    while res not in 'sn':
        res = input('Deseja comprar outro produto? ').strip().lower()[0]
    soma += preco
    contP += 1
    if preco > 1000:
        cont += 1
    if mbarato == '' or preco < p:
        mbarato = nome
        p = preco
    if res == 'n': break
print(f'Você comprou {contP} produtos e total da compra é R${soma:.2f}')
print(f'{cont} produtos custam mais de R$1000,00')
print(f'O produto mais barato é {mbarato} e custa R${p:.2f}')