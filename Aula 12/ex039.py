from datetime import date, datetime

nasc = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
id = atual - nasc
print(f'Por ter nascido em {nasc} você tem {id} anos em {atual}.')

if id < 18:
    print(f'Ainda faltam {18 - id} anos para o seu alistamento, você deve se alistar em {atual + (18 - id)}.')
elif id == 18:
    print('Esse é o ano do seu alimentamento! Inscreva-se imediatamente.')
else:
    print(f'Você deveria ter se alistado há {id - 18} anos.')
    print(f'O alistamento para nascidos em {nasc} foi no ano de {atual - (id - 18)}.')