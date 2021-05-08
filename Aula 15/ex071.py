print('* *' * 10)
print(f'{"BANCO DO PROGRAMADOR":^30}')
print('* *' * 10)
valor = int(input('Deseja sacar qual valor? R$'))
ced = 100
totced = 0
print(f'{"TOTAL DE NOTAS DO SAQUE":^30}')
while True:
    if valor >= ced:
        totced = valor // ced
        valor -= (totced * ced)
    else:
        if totced > 0:
            print(f'{totced:^3} notas de R${ced:.2f}')
            totced = 0
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        if valor == 0:
            break