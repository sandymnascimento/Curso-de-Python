x = int(input('Deseja conhecer a tabuada de qual número? '))
print('=' * 15)
print(f'|TABUADA DO {x} |')
print('=' * 15)
for c in range(1, 11):
    print(f'| {x} x {c:2} = {x*c:2} |')
print('=' * 15)
