from random import randint
from time import sleep

palpites = list()
cont = 0
print('=' * 29)
print('  PALPITES PARA A MEGA SENA')
print('=' * 29)
x = int(input('Quantos jogos você quer sortear? '))
print('* ' * 16)
print(f'      SORTEANDO {x} JOGOS')
print('* ' * 16)
for i in range(0, x):
    palpites.append(list())
    while True:
        x = randint(0, 60)
        if x not in palpites[i]:
            palpites[i].append(x)
            cont += 1
        if cont == 6:
            cont = 0
            break
    sleep(1)
    palpites[i].sort()
    print(f'Jogo {i + 1}: {palpites[i]}')
sleep(0.5)
print('* ' * 16)
print('          BOA SORTE!')
print('* ' * 16)
