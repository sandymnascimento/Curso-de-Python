pessoas = list()
dados = list()
maior = menor = 0
while True:
    dados.append(input('Nome: '))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    elif dados[1] > maior:
        maior = dados[1]
    elif dados[1] < menor:
        menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    res = input('Deseja continuar? ').strip()[0]
    if res in 'Nn':
        break
print(f'Você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso cadastrado foi: {maior:.2f}. Pessoas com esse peso: ', end='')
for p in pessoas:
    if maior == p[1]:
        print(f'[ {p[0]} ]')
print(f'O menor peso foi cadastrado foi: {menor:.2f}. Pessoas com esse peso: ', end='')
for p in pessoas:
    if menor == p[1]:
        print(f'[ {p[0]} ]')

