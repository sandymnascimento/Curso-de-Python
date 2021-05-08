from random import randint
print('\033[1;34m* ' * 20)
print(' '* 5, 'Vamos jogar PAR ou ÍMPAR?')
print('\033[1;34m* \033[m' * 20)
cont = 0
while True:
    user = input('Você escolhe PAR ou IMPAR? ').strip().lower()[0]
    numuser = int(input('Digite um valor: '))
    numpc = randint(0, 10)
    print(f'Você escolheu {numuser} e eu escolhi {numpc}, total de {numpc + numuser}.')
    if (numuser + numpc) % 2 == 0:
        if user == 'i':
            print('O total é PAR, você perdeu!')
            break
        else:
            print('O total é PAR, você venceu! Vamos jogar novamente!')
            cont += 1
    else:
        if user == 'p':
            print('O total é ÍMPAR, você perdeu!')
            break
        else:
            print('O total é ÍMPAR, você venceu! Vamos jogar novamente!')
            cont += 1
print('\033[1;31m* ' * 24)
print(f' GAME OVER! Você teve {cont} vitórias consecutivas.')
print('\033[1;31m* \033[m' * 24)