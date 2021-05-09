ano = int(input('Digite um ano e descubra se ele é bissexto: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é um ano bissexto, possui 366 dias!')
else:
    print(f'O ano {ano} não é um ano bissexto, possui 365 dias!')
