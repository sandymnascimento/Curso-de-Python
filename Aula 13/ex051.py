print('=' * 21)
print('\033[1m 10 TERMOS DE UMA PA')
print('=' * 21)

x = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
déc = x + (10 - 1) * r
for c in range(x, déc + r, r):
    print(c, end=' 🠖 ')
print('FIM')