from random import randint

n = randint(0, 5)
print('Tente descobrir qual o número que o computador está "pensando"!')
x = int(input('Digite um número entre 0 e 5: '))
if n == x:
    print('Parabens! Você acertou o número.')
else:
    print(f'Que pena! Você errou, o número era {n}. Tente novamente!')
