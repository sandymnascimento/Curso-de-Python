km = int(input('Qual a distância da sua viagem (em Km)? '))
if km <= 200:
    p = km * 0.50
else:
    p = km * 0.45
print(f'O valor da passagem para uma viagem de {km}km é R${p:.2f}')
