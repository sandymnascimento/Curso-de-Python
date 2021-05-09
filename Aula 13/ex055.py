sidade = 0
cont = 0
idhomem = 0
maisv = ''
for c in range(1, 5):
    print(f"---- {c}ª PESSOA ----")
    nome = input('Nome: ').strip()
    id = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    sidade += id
    if sexo == 'F' and id < 20:
        cont += 1
    if sexo == 'M' and id > idhomem:
        idhomem = id
        maisv = nome
print('\033[1m-' * 20)
print('Resultado da análise')
print('\033[1m-\033[m' * 20)
print(f'A média de idade do grupo é de {(sidade / 4)} anos.')
if maisv != '':
    print(f'O homem mais velho do grupo tem {idhomem} anos e se chama {maisv}.')
print(f'O grupo contém {cont} mulheres com menos de 20 anos.')