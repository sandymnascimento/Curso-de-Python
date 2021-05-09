print('\033[1;7;40mConversor de bases numéricas.\033[m')
x = int(input('Digite o valor que deseja converter: '))
b = int(input('[ 1 ] - para binário.\n[ 2 ] - para octal.\n[ 3 ]- para hexadecimal.\nEscolha agora a base desejada: '))

if b == 1:
    print(f'O número {x} convertido para binário é: {x:06b}.')
elif b == 2:
    print(f'O número {x} convertido para octal é: {x:o}.')
elif b == 3:
    print(f"O número {x} convertido para hexadecimal é: {x:x}.")
else:
    print('O valor digitado é inválido.')