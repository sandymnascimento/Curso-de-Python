while True:
    x = int(input('Deseja conhecer a tabuada de qual número? '))
    if x < 0: break
    print('=' * 15)
    print('|TABUADA DO {} |'.format(x))
    print('=' * 15)
    for c in range (1, 11):
        print('| {} x {:2} = {:2} |'.format(x, c, x * c))
    print('=' * 15)
print('PROGRAMA TABUADA ENCERRADO.')