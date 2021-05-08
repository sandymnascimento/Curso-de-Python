print('* ' * 13)
print(' Sequência de Fibonacci')
print('* ' * 13)
n = int(input('Digite o termo: '))
cont = 3
atual = 0
prox = 1
print(f'{atual} 🠖 {prox}  🠖', end = ' ')
while cont <= n:
    seq = atual + prox
    print(seq, end=' 🠖 ')
    atual = prox
    prox = seq
    cont += 1
print('FIM.')