from random import randint
from time import sleep
from operator import itemgetter

temp = 0
dados = dict()
dados['Jogador1'] = randint(1, 6)
dados['Jogador2'] = randint(1, 6)
dados['Jogador3'] = randint(1, 6)
dados['Jogador4'] = randint(1, 6)
print('Sorteando...')
sleep(0.5)
print('Valores sorteados:')
for k, v in dados.items():
    print(f'    O {k} tirou {v}')
    sleep(1)

ranking = list()
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
sleep(0.5)
print('Ranking dos jogadores')
sleep(0.5)
for k, v in enumerate(ranking):
    print(f'    {k + 1}o lugar: {v[0]} com {v[1]}.')
    sleep(1)