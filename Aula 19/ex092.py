from datetime import datetime
ficha = dict()
ficha['nome'] = input('Nome: ')
id = int(input('Ano de nascimento: '))
ficha['idade'] = datetime.today().year - id
ficha['ctps'] = int(input('Carteira de trabalho (0 se não possuir): '))
if ficha['ctps'] != 0:
    ficha['ano'] = int(input('Ano de contratação: '))
    ficha['sal'] = float(input('Salário: R$'))
    ficha['apos'] = (ficha['ano'] + 35) - id
print('=' * 23)
print('INFORMAÇÕES CADASTRADAS')
print('=' * 23)
print(f'Nome: {ficha["nome"]}.')
print(f'Idade: {ficha["idade"]}.')
if ficha['ctps'] == 0:
    print(f'Usuário não possui carteira de trabalho.')
else:
    print(f'Carteira de trabalho: {ficha["ctps"]}.')
    print(f'Foi contratado no ano de {ficha["ano"]}.')
    print(f'Possui um salário de R${ficha["sal"]:.2f}.')
    print(f'Poderá se aposentar aos {ficha["apos"]} anos.')