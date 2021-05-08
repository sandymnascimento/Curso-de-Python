print('=' * 21)
print('\033[1m 10 TERMOS DE UMA PA')
print('=' * 21)
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
dec = p + (10 - 1) * r
while p <= dec:
    print(p, end = ' 🠖 ')
    p += r
print('FIM!')