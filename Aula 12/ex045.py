from random import choice
print('\033[34m=\033[m' * 20)
print('\033[1;30;44mVamos jogar JOKENPÔ!\033[m')
print('\033[34m=\033[m' * 20)
jogo = ['pedra', 'papel', 'tesoura']
pc = choice(jogo)
print('Já escolhi o que vou jogar!')
res = input('Você quer pedra, papel ou tesoura? ').lower()

if pc == res:
    print(f'Nós dois escolhemos {pc}! Deu empate.')
elif pc == 'pedra' and res == 'tesoura' or pc == 'tesoura' and res == 'papel' or pc == 'papel' and res == 'pedra':
    print(f'Há Há! Ganhei! Escolhi {pc} que ganha do(a) {res}.')
else:
    print(f'Poxa, dessa vez você me venceu! Eu escolhi {pc} que perde para {res}.')