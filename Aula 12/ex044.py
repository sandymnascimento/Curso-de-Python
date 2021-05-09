preco = float(input('Digite o preço do produto: '))
cond = int(input('\033[1;4mFormas de pagamento:\033[m\n'
                 '\033[1;7m1\033[m - à vista dinheiro/cheque.\n'
                 '\033[1;7m2\033[m - à vista no cartão.\n'
                 '\033[1;7m3\033[m - em até 2x no cartão.\n'
                 '\033[1;7m4\033[m - 3x ou mais no cartão.\n'
                 'Digite a opção desejada: '))

if cond == 1:
    tot = preco * 0.9
    print(f'Você terá 10% de desconto, o valor a ser pago pelo produto é de R${preco:.2f}.')
elif cond == 2:
    tot = preco * 0.95
    print(f'Você terá 5% de desconto, o valor a ser pago pelo produto é de R${preco:.2f}.')
elif cond == 3:
    print(f'O valor a ser pago pelo produto é de R${preco:.2f} em 2 parcelas de {preco / 2:.2f}.')
elif cond == 4:
    tot = preco * 1.2
    print(f'Essa opção de pagamento possui juros de 20%, o valor a ser pago pelo produto é de R${preco:.2f}')
else:
    print('Opção inválida.')
print(f'Sua compra de R${preco:.2f} vai custar R${tot:.2f} no final.')
