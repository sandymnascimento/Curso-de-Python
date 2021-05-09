print('Realizaremos o calculo para aumento de salário!')
x = float(input('Digite o seu sálario atual: '))

if x <= 1250.00:
    print(f'Você recebeu um aumento de 15%! Seu novo salário é de R${x * 1.15:.2f}')
else:
    print(f'Você recebeu um aumento de 10%! Seu novo salário é de R${x * 1.10:.2f}')