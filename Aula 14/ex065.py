res = 'S'
cont = soma = maior = menor = 0
while res == 'S':
    x = int(input('Digite um número: '))
    res = input('Deseja continuar? [sim/nao]').strip().upper()[0]
    if cont == 0:
        maior = menor = x
    if x > maior:
        maior = x
    elif x < menor:
        menor = x
    cont += 1
    soma += x
print(f'Foram lidos {cont} números, a média entre eles é de {soma/cont}.')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')