var = input('Digite algo: ')
print('O tipo primitivo do conteúdo é: ', type(var))
print('O conteúdo é composto apenas por letras? ', var.isalpha())
print('O conteúdo é composto apenas por números? ', var.isnumeric())
print('O conteúdo é alhpanumérico? ', var.isalnum())
print('O conteúdo esta em maiúsculo? ', var.isupper())
print('O conteúdo está em minúsculo?', var.islower())

