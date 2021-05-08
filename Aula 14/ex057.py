sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F': # sexo not in 'MmFf'
    sexo = input('Dados inválidos. Por favor, informe seu sexo [M/F]: ').strip().upper()[0]
if sexo in 'M':
    print('Sexo masculino registrado com sucesso!')
else:
    print('Sexo feminino registrado com sucesso!')
