v = int(input('Digite a velocidade do carro: '))
if v > 80:
    print('Você foi MULTADO por excesso de velocidade! O limite é de 80 km/h.')
    print(f'Você deve pagar uma multa no valor de R${(v - 80) * 7},00.')
print('Dirija com segurança!')
