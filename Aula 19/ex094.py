dados = dict()
pessoas = list()
totid = 0
while True:
    dados['nome'] = input('Nome: ').strip()
    dados['id'] = int(input('Idade: '))
    while True:
        dados['sexo'] = input('Sexo: [M/F] ').strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite feminino (f) ou masculino (m).')
    totid += dados['id']
    pessoas.append(dados.copy())

    while True:
        res = input('Deseja continuar? ').strip()[0]
        if res in 'SsNn':
            break
        print('ERRO! Por favor, responda apenas sim ou não.')
    if res in 'Nn':
        break
print('ANÁLISE DO GRUPO:\n')
print(f'A)   Ao todo temos {len(pessoas)} cadastradas.')
print(f'B)   A média de idade é de {totid / len(pessoas)} anos.')
print('C)   As mulheres cadastradas foram: ', end='')
for c in pessoas:
    if c['sexo'] in 'F':
        print(f'{c["nome"]}.', end=' ')
print()
print('D)   Lista de pessoas acima da média de idade:')
for c in pessoas:
    if c['id'] > (totid / len(pessoas)):
        print(f'    Nome: {c["nome"]}; Idade: {c["id"]}; Sexo: {c["sexo"]}.')
print('<<<ENCERRADO>>>')