from datetime import date
ano = date.today().year
contmaior = 0
contmenor = 0
for c in range (1, 8):
    x = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if ano - x >= 18:
        contmaior += 1
    else:
        contmenor += 1
print(f'Dos sete, {contmaior} pessoas são maiores de idade (+= 18 anos), e {contmenor} são menores de idade.')