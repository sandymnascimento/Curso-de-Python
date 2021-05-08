from time import sleep
x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))
op = 0
while op != 5:
    print('* ' * 16)
    print('[ 1 ] Somar\n[ 2 ] Multiplicar')
    print('[ 3 ] Maior entre os números')
    print('[ 4 ] Digitar novos números')
    print('[ 5 ] Encerrar o programa')
    op = int(input('\033[1mDigite a operação desejada: \033[m'))
    print('* ' * 16)
    if op == 1:
        print(f'  O resultado de {x} + {y} é {x + y}.')
    elif op == 2:
        print(f'  O resultado de {x} x {y} é {x * y}.')
    elif op == 3:
        if x > y: maior = x
        else: maior = y
        print(f'O maior número entre {x} e {y} é {maior}.')
    elif op == 4:
        x = int(input('Digite o novo valor: '))
        y = int(input('Digite o novo valor: '))
    elif op == 5:
        print('Finalizando', end='')
        break
    else:
        print('\033[1mOPÇÃO INVÁLIDA. Tente novamente.\033[m')

for c in range(0, 3):
    print('.', end=' ')
    sleep(0.5)
print('Programa encerrado.')