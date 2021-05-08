num = list()
while True:
    x = int(input('Digite um valor: '))
    if x in num:
        print('Esse valor já foi adicionado a listagem.')
    else:
        num.append(x)
        print('Valor adicionado com sucesso!')
    res = input('Deseja adicionar outro valor? [s/n]').strip().lower()[0]
    if res == 'n':
        break
num.sort()
print(f'Você digitou os seguintes valores: {num}')
