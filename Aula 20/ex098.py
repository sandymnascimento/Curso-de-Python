from time import sleep


def contador(ini, fim, p):
    print(f'Contagem de {ini} até {fim} de {abs(p)} em {abs(p)}')
    sleep(2)
    if ini < fim:
        for c in range(ini, fim + 1, p):
            print(c, end=' ')
            sleep(0.5)
        print('FIM!')
        print('=-' * 20)
    else:
        for c in range(ini, fim - 1, -abs(p)):
            sleep(0.5)
            print(c, end=' ')
        print('FIM!')
        print('=-' * 20)


print('=-' * 20)
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input(f'{"Digite o inicio: ":<16}'))
f = int(input(f'{"Digite o fim: ":<17}'))
p = int(input(f'{"Digite o passo: ":<17}'))
if p == 0:
    p = 1
contador(i, f, p)