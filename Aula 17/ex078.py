num = list()
maior = menor = 0
for c in range(0, 5):
    num.append(int(input(f'Digite o valor para a posição {c}: ')))
print(f'Você digitou os valores: {num}')
print(f'O maior valor digitado foi [ {max(num)} ] e ele está nas posiçoes: ', end='')
for i, v in enumerate(num):
    if v == max(num):
        print(f'{i}.', end=' ')
print(f'\nO menor valor digitado foi [ {min(num)} ] e ele está nas posiçoes: ', end='')
for i, v in enumerate(num):
    if v == min(num):
        print(f'{i}.', end=' ')