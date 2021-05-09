from datetime import date
print(' \033[1;30;46m=== CONFEDERAÇÃO DE NATAÇÃO ===\033[m')
ano = date.today().year
nasc = int(input('Digite o ano de nascimento do atleta: '))
id = ano - nasc
print(f'Atletas nascidos em {nasc} tem {id} anos em {ano}.')

if id <= 9:
    print('O atleta será inscrito na categoria MIRIM.')
elif id <= 14:
    print('O atleta será inscrito na categoria INFANTIL')
elif id <= 19:
    print('O atleta será inscrito na categoria JÚNIOR')
elif id <= 25:
    print('O atleta será inscrito na categoria SÊNIOR')
else:
    print('O atleta será inscrito na categoria MASTER')