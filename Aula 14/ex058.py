from random import randint
from time import sleep

cont = 1
print(' ' * 15, '\033[1;35m *' * 15)
print(' ' * 25, 'VAMOS JOGAR?')
print(' ' * 15, '\033[1;35m *\033[m' * 15)
sleep(1)
print('Pensarei em um número de 0 a 10 e você deve tentar adivinhar qual foi!')
pc = randint(0, 10)
sleep(2)
user = int(input('Pronto! Já pensei! Qual número você acha que eu escolhi? '))

while pc != user:
    if pc < user:
        print('O número é menor... Tente mais uma vez.')
    else:
        print('O número é maior... Tente mais uma vez.')
    user = int(input('Qual número acha que eu escolhi? '))
    cont += 1

print(f'Foram necessárias {cont} tentativas para você acertar! Parabéns :)')
