x = int(input('Digite um valor entre 0 e 9999: '))
u = x % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10

print(f'Unidade: {u}.')
print(f'Dezena: {d}.')
print(f'Centena: {c}.')
print(f'Milhar: {m}.')
