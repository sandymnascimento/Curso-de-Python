print('=' * 21)
print('\033[1m 10 TERMOS DE UMA PA')
print('=' * 21)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
cont = 1
c = 10
while cont <= c:
    print(p, end=' 🠖 ')
    p += r
    if cont == c:
        print('PAUSA')
        x = int(input('Quantos termos você quer mostrar a mais? '))
        c += x
    cont += 1

print(f'A progressão foi finalizada com {cont - 1} termos exibidos.')
