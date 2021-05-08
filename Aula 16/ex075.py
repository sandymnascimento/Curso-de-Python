num = (int(input('Digite o 1º valor: ')), int(input('Digite o 2º valor: ')), int(input('Digite o 3º valor: ')), int(input('Digite o 4º valor: ')))
print(f'Você digitou os valores {num}')
print(f'O número "9" apareceu {num.count(9)} vezes nessa listagem.')
if 3 in num:
    print(f'O número "3" aparece na {num.index(3) + 1}ª posição .')
else:
    print('O número 3 não foi digitado.')
print('Os números pares digitados foram: ', end='')
for c in range(0, 4):
    if num[c] % 2 == 0:
        print(num[c], end=' ')
