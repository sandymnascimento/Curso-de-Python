jogador = dict()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')
    x = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = list()
    for c in range(1, x + 1):
        jogador['gols'].append(int(input(f'Ele fez quantos gols na partida {c}? ')))
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())
    while True:
        res = input('Deseja continuar? ').strip()[0]
        if res in 'SsNn':
            break
        print('ERRO! Por favor, responda apenas sim ou não.')
    if res in 'Nn':
        break
print('= ' * 30)
print(f'{"INFORMAÇÕES DE DESEMPENHO DO TIME":>45}')
print('= ' * 30)
print(f'{"COD":<5}{"Nome":<20}{"Gols":<20}{"Total":<5}')
for k, j in enumerate(time):
    print(f'{k:<5}', end='')
    for v in j.values():
        print(f'{str(v):<20}', end='')
    print()
while True:
    r = int(input('Digite o código do jogador para mais informações [999 para encerrar]: '))
    if r == 999:
        print('Finalizando...')
        break
    if r not in enumerate(time):
        print('ERRO! Código de jogador inválido.')
    else:
        print(f'>>> RENDIMENTO DO JOGADOR {time[r]["nome"]}:')
        for k, v in enumerate(time[r]['gols']):
            print(f'    Na partida {k+1}, fez {v} gols.')
print('<<PROGRAMA ENCERRADO.>>')