jogador = dict()
jogador['nome'] = input('Nome do jogador: ')
x = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = list()
for c in range(1, x + 1):
    jogador['gols'].append(int(input(f'Ele fez quantos gols na partida {c}? ')))
jogador['total'] = sum(jogador['gols'])
print('= ' * 30)
print(f'{"INFORMAÇÕES DE DESEMPENHO":>42}')
print('= ' * 30)
print(jogador)
print('= ' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('= ' * 30)
print(f'O jogador {jogador["nome"]} jogou {x} partidas, com um total de {jogador["total"]} gols.')
for k, v in enumerate(jogador['gols']):
    print(f'    => Na partida {k+1}, fez {v} gols.')
print('= ' * 30)