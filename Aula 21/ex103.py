def ficha(nome, gols=0):
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0

    if nome == '':
        return f'O jogador <desconhecido> fez {gols} gol(s) no campeonato.'
    else:
        return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


print(ficha(input('Nome do jogador: ').strip(), input('Gols no campeonato: ')))
