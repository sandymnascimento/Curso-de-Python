totid = homens = mulheres = cont = 0
while True:
    print('-' * 19)
    print('CADASTRE UMA PESSOA')
    print('-' * 19)
    id = int(input('Digite a idade: '))
    while sex not in 'mf':
        sex = input('Digite o sexo: ').strip().lower()[0]
    while res not in 'sn':
        res = input('Realizar outro cadastro? ').strip().lower()[0]
    cont += 1
    if id >= 18:
        totid += 1
    if sex == 'm':
        homens += 1
    elif sex == 'f' and id < 20:
        mulheres += 1
    if res == 'n': break
print(f'Foram lidos os dados de {cont} pessoas, e desse número {totid} tem mais de 18 anos.')
print(f'Foram cadastrados {homens} homens, e um total de {mulheres} mulheres cadastradas tem menos de 20 anos.')
