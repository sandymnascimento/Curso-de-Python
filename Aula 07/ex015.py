dias = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos Km foram percorridos nesse período? '))
valor =float(60 * dias + 0.15 * km)
print('O aluguel custa R$60,00 por dia e R$0,15 por km percorrido.')
print(f'Por ter utilizado o carro por {dias} dias e percorrido {km} km, o valor a ser pago é de RS{valor:.2f}')
