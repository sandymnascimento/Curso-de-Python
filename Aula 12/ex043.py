print('*-*' * 9)
print(f'{" ":4}\033[1;7mCALCULADORA DE IMC\033[m')
print('*-*' * 9)

peso = float(input('Digite o seu peso: '))
alt = float(input('Digite a sua altura: '))
IMC = peso / (alt * alt)
print(f'O seu IMC é: {IMC:.2f}.')
if IMC < 18.5:
    print('Você está abaixo do peso! Procure ajuda profissional.')
elif IMC < 25:
    print('Parabéns, você se encontra na faixa de peso ideal.')
elif IMC < 30:
    print('Você está em sobrepeso.')
elif IMC < 40:
    print('Você está em obesidade. Procure ajuda profissional.')
else:
    print('Você está em obesidade mórbida. Procure ajuda profissional.')